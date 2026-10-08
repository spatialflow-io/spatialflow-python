"""
Pagination helpers for SpatialFlow SDK.

Provides async iterators for paginated API responses.
"""

from typing import TypeVar, Generic, AsyncIterator, Callable, Awaitable, Any, List, Optional

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
        next_url: Optional[str] = None,
        previous_url: Optional[str] = None,
    ):
        self.items = items
        self.count = count
        self.next_url = next_url
        self.previous_url = previous_url

    @property
    def has_more(self) -> bool:
        return self.next_url is not None

    def __iter__(self):
        """Iterates over items in the current page only."""
        return iter(self.items)

    def __len__(self) -> int:
        """Number of items in the current page, not the total count."""
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
        extract_next: Callable[[Any], Optional[str]],
        limit: int = 100,
    ):
        """
        Args:
            fetch_page: Async function taking (offset, limit) and returning a page response
        """
        self._fetch_page = fetch_page
        self._extract_items = extract_items
        self._extract_count = extract_count
        self._extract_next = extract_next
        self._limit = limit
        self._offset = 0
        self._exhausted = False
        self._total_count: Optional[int] = None
        self._uses_cursor: Optional[bool] = None

    async def __aiter__(self) -> AsyncIterator[T]:
        """Iterates over items across all pages, fetching each page lazily."""
        while not self._exhausted:
            response = await self._fetch_page(self._offset, self._limit)
            items = self._extract_items(response)
            self._total_count = self._extract_count(response)
            next_url = self._extract_next(response)

            for item in items:
                yield item

            # Whether this API uses cursor-based pagination is only knowable once
            # a page with items has told us whether a next_url comes back.
            if self._uses_cursor is None and len(items) > 0:
                self._uses_cursor = next_url is not None

            if len(items) < self._limit:
                self._exhausted = True
            elif self._uses_cursor and next_url is None:
                self._exhausted = True
            else:
                self._offset += self._limit

    @property
    def total_count(self) -> Optional[int]:
        """Total count of items; None until the first page has been fetched."""
        return self._total_count


def paginate(
    fetch_page: Callable[[int, int], Awaitable[Any]],
    limit: int = 100,
    *,
    items_field: str = "geofences",
) -> AsyncPaginator:
    """
    Generic paginator for offset-based pagination. Use the resource-specific
    helpers (paginate_geofences, paginate_workflows, etc.) for convenience.

    Args:
        items_field: Name of the field containing items in the response

    Example:
        >>> async def fetch(offset, limit):
        ...     return await client.geofences.apps_geofences_api_list_geofences(
        ...         offset=offset, limit=limit
        ...     )
        >>> async for geofence in paginate(fetch, items_field="geofences"):
        ...     print(geofence.name)
    """
    return AsyncPaginator(
        fetch_page=fetch_page,
        extract_items=lambda r: getattr(r, items_field, []),
        extract_count=lambda r: getattr(r, "count", 0),
        extract_next=lambda r: None,  # Offset-based pagination, no next URL
        limit=limit,
    )


def paginate_geofences(
    fetch_page: Callable[[int, int], Awaitable[Any]],
    limit: int = 100,
) -> AsyncPaginator:
    """
    Create a paginator for geofence list endpoints.

    Returns:
        AsyncPaginator that yields GeofenceResponse objects

    Example:
        >>> async def fetch(offset, limit):
        ...     return await client.geofences.apps_geofences_api_list_geofences(
        ...         offset=offset, limit=limit
        ...     )
        >>> async for geofence in paginate_geofences(fetch):
        ...     print(geofence.name)
    """
    return AsyncPaginator(
        fetch_page=fetch_page,
        extract_items=lambda r: r.geofences,
        extract_count=lambda r: r.total_count,
        extract_next=lambda r: None,
        limit=limit,
    )


def paginate_workflows(
    fetch_page: Callable[[int, int], Awaitable[Any]],
    limit: int = 100,
) -> AsyncPaginator:
    """
    Create a paginator for workflow list endpoints.

    Returns:
        AsyncPaginator that yields WorkflowListOut objects
    """
    return AsyncPaginator(
        fetch_page=fetch_page,
        extract_items=lambda r: r.workflows,
        extract_count=lambda r: r.total,
        extract_next=lambda r: None,
        limit=limit,
    )


def paginate_webhooks(
    fetch_page: Callable[[int, int], Awaitable[Any]],
    limit: int = 100,
) -> AsyncPaginator:
    """
    Create a paginator for webhook list endpoints.

    Returns:
        AsyncPaginator that yields WebhookResponse objects
    """
    return AsyncPaginator(
        fetch_page=fetch_page,
        extract_items=lambda r: r.webhooks,
        extract_count=lambda r: r.pagination.get("total", 0),
        extract_next=lambda r: None,
        limit=limit,
    )
