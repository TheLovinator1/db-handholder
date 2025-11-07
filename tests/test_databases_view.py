from typing import TYPE_CHECKING

import pytest

from databases.models import DatabaseInstance

if TYPE_CHECKING:
    from django.test import Client

    from databases.views import HttpResponse


@pytest.mark.django_db
class TestDatabaseListViewEmpty:
    def test_list_view_shows_empty_state(self, client: Client) -> None:
        response: HttpResponse = client.get("/databases")
        assert response.status_code == 200, f"Response content: {response.content.decode()}"
        content: str = response.content.decode()
        assert "No databases" in content, f"Response content: {content}"


@pytest.mark.django_db
class TestDatabaseListView:
    @pytest.fixture(autouse=True)
    def setup_data(self) -> None:
        DatabaseInstance.objects.create(name="reporting-db", db_type="postgresql")
        DatabaseInstance.objects.create(name="cache", db_type="redis")

    def test_list_view_returns_200_and_lists_items(self, client: Client) -> None:
        response: HttpResponse = client.get("/databases")
        assert response.status_code == 200, f"Response content: {response.content.decode()}"
        html: str = response.content.decode()
        assert "reporting-db" in html, f"Response HTML was: {html}"
        assert "cache" in html, f"Response HTML was: {html}"
        assert "PostgreSQL" in html, f"Response HTML was: {html}"
        assert "Redis" in html, f"Response HTML was: {html}"

    def test_list_view_without_trailing_slash_also_works(self, client: Client) -> None:
        response: HttpResponse = client.get("/databases")
        assert response.status_code == 200, f"Response content: {response.content.decode()}"
