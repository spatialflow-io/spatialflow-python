"""Tests for pagination helpers."""

import pytest

from spatialflow import paginate, AsyncPaginator, PaginatedResponse


class MockResponse:
    """Mock API response with results, count, next attributes."""

    def __init__(self, results, count, next=None):
        self.results = results
        self.count = count
        self.next = next


class TestPaginate:
    """Test the paginate async generator."""

    async def test_paginate_all_items(self):
        """Test that paginate yields all items across pages."""
        responses = [
            MockResponse(
                results=[{"id": 1, "name": "First"}, {"id": 2, "name": "Second"}],
                count=5,
                next="http://api/items?offset=2",
            ),
            MockResponse(
                results=[{"id": 3, "name": "Third"}, {"id": 4, "name": "Fourth"}],
                count=5,
                next="http://api/items?offset=4",
            ),
            MockResponse(
                results=[{"id": 5, "name": "Fifth"}],
                count=5,
                next=None,
            ),
        ]
        page_index = 0

        async def fetch_page(offset: int, limit: int):
            nonlocal page_index
            response = responses[page_index]
            page_index += 1
            return response

        items = []
        async for item in paginate(fetch_page, limit=2, items_field="results"):
            items.append(item)

        assert len(items) == 5
        assert items[0]["name"] == "First"
        assert items[4]["name"] == "Fifth"

    async def test_paginate_empty_results(self):
        """Test pagination with empty results."""

        async def fetch_page(offset: int, limit: int):
            return MockResponse(results=[], count=0, next=None)

        items = []
        async for item in paginate(fetch_page, items_field="results"):
            items.append(item)

        assert len(items) == 0

    async def test_paginate_single_page(self):
        """Test pagination with only one page."""

        async def fetch_page(offset: int, limit: int):
            return MockResponse(
                results=[{"id": 1}, {"id": 2}],
                count=2,
                next=None,
            )

        items = []
        async for item in paginate(fetch_page, items_field="results"):
            items.append(item)

        assert len(items) == 2

    async def test_paginate_respects_limit(self):
        """Test that paginate uses the provided limit."""
        captured_limits = []

        async def fetch_page(offset: int, limit: int):
            captured_limits.append(limit)
            return MockResponse(results=[], count=0, next=None)

        async for _ in paginate(fetch_page, limit=50, items_field="results"):
            pass

        assert captured_limits == [50]

    async def test_paginate_default_limit(self):
        """Test that paginate uses default limit of 100."""
        captured_limits = []

        async def fetch_page(offset: int, limit: int):
            captured_limits.append(limit)
            return MockResponse(results=[], count=0, next=None)

        async for _ in paginate(fetch_page, items_field="results"):
            pass

        assert captured_limits == [100]


class TestAsyncPaginator:
    """Test the AsyncPaginator class."""

    async def test_async_paginator_iteration(self):
        """Test AsyncPaginator async iteration."""
        call_count = 0

        async def fetch_page(offset: int, limit: int):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return MockResponse(
                    results=[{"id": 1}],
                    count=2,
                    next="http://api?offset=1",
                )
            return MockResponse(
                results=[{"id": 2}],
                count=2,
                next=None,
            )

        paginator = AsyncPaginator(
            fetch_page=fetch_page,
            extract_items=lambda r: r.results,
            extract_count=lambda r: r.count,
            extract_next=lambda r: r.next,
            limit=1,
        )
        items = []
        async for item in paginator:
            items.append(item)

        assert len(items) == 2
        assert call_count == 2


class TestPaginatedResponse:
    """Test the PaginatedResponse class."""

    def test_paginated_response_creation(self):
        """Test PaginatedResponse can be created with all fields."""
        response = PaginatedResponse(
            items=[1, 2, 3],
            count=10,
            next_url="http://next",
            previous_url="http://prev",
        )

        assert response.items == [1, 2, 3]
        assert response.count == 10
        assert response.next_url == "http://next"
        assert response.previous_url == "http://prev"
        assert response.has_more is True

    def test_paginated_response_optional_fields(self):
        """Test PaginatedResponse with optional fields omitted."""
        response = PaginatedResponse(
            items=[],
            count=0,
        )

        assert response.items == []
        assert response.count == 0
        assert response.next_url is None
        assert response.previous_url is None
        assert response.has_more is False

    def test_paginated_response_iteration(self):
        """Test that PaginatedResponse can be iterated."""
        response = PaginatedResponse(
            items=[{"id": 1}, {"id": 2}],
            count=2,
        )

        items = list(response)
        assert len(items) == 2

    def test_paginated_response_len(self):
        """Test that len() works on PaginatedResponse."""
        response = PaginatedResponse(
            items=[1, 2, 3],
            count=10,
        )

        assert len(response) == 3
