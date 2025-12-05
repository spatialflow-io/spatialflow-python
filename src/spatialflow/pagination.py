"""
Pagination helpers for SpatialFlow SDK.

Provides async iterators for paginated API responses.
"""

from typing import TypeVar, Generic, AsyncIterator, Callable, Awaitable, Any, List

T = TypeVar("T")


class PaginatedResponse(Generic[T]):
    """
    A paginated response with helper methods for navigation.

    Attributes:
        items: The items in the current page
        count: Total number of items across all pages
        next_url: URL for the next page (if any)
        previous_url: URL for the previous page (if any)
    """

    def __init__(
        self,
        items: List[T],
        count: int,
        next_url: str | None = None,
        previous_url: str | None = None,
    ):
        self.items = items
        self.count = count
        self.next_url = next_url
        self.previous_url = previous_url

    @property
    def has_more(self) -> bool:
        """Returns True if there are more pages available."""
        return self.next_url is not None

    def __iter__(self):
        """Iterate over items in the current page."""
        return iter(self.items)

    def __len__(self) -> int:
        """Number of items in the current page."""
        return len(self.items)


class AsyncPaginator(Generic[T]):
    """
    Async iterator for paginated API responses.

    Automatically fetches subsequent pages as you iterate.

    Example:
        >>> async for geofence in client.geofences.list_all():
        ...     print(geofence.name)
    """

    def __init__(
        self,
        fetch_page: Callable[[int, int], Awaitable[Any]],
        extract_items: Callable[[Any], List[T]],
        extract_count: Callable[[Any], int],
        extract_next: Callable[[Any], str | None],
        limit: int = 100,
    ):
        """
        Initialize the paginator.

        Args:
            fetch_page: Async function that fetches a page (offset, limit) -> response
            extract_items: Function to extract items list from response
            extract_count: Function to extract total count from response
            extract_next: Function to extract next page URL from response
            limit: Number of items per page
        """
        self._fetch_page = fetch_page
        self._extract_items = extract_items
        self._extract_count = extract_count
        self._extract_next = extract_next
        self._limit = limit
        self._offset = 0
        self._exhausted = False
        self._total_count: int | None = None

    async def __aiter__(self) -> AsyncIterator[T]:
        """Async iterate over all items across all pages."""
        while not self._exhausted:
            response = await self._fetch_page(self._offset, self._limit)
            items = self._extract_items(response)
            self._total_count = self._extract_count(response)
            next_url = self._extract_next(response)

            for item in items:
                yield item

            if next_url is None or len(items) < self._limit:
                self._exhausted = True
            else:
                self._offset += self._limit

    @property
    def total_count(self) -> int | None:
        """
        Total count of items (available after first page is fetched).
        """
        return self._total_count


def paginate(
    fetch_page: Callable[[int, int], Awaitable[Any]],
    limit: int = 100,
) -> AsyncPaginator:
    """
    Create a paginator for a list endpoint.

    This is a convenience function for the common case where the response
    has 'results', 'count', and 'next' fields.

    Args:
        fetch_page: Async function that takes (offset, limit) and returns response
        limit: Number of items per page (default 100)

    Returns:
        AsyncPaginator that yields items from all pages

    Example:
        >>> async def fetch(offset, limit):
        ...     return await client.geofences.apps_geofences_api_list_geofences(
        ...         offset=offset, limit=limit
        ...     )
        >>> async for geofence in paginate(fetch):
        ...     print(geofence.name)
    """
    return AsyncPaginator(
        fetch_page=fetch_page,
        extract_items=lambda r: r.results if hasattr(r, "results") else [],
        extract_count=lambda r: r.count if hasattr(r, "count") else 0,
        extract_next=lambda r: r.next if hasattr(r, "next") else None,
        limit=limit,
    )
