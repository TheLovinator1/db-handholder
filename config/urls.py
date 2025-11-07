from typing import TYPE_CHECKING

from debug_toolbar.toolbar import debug_toolbar_urls  # pyright: ignore[reportMissingTypeStubs]
from django.urls import include
from django.urls import path

if TYPE_CHECKING:
    from django.urls.resolvers import URLResolver

urlpatterns: list[URLResolver] = [
    path(route="__reload__/", view=include("django_browser_reload.urls")),
    path("", include("databases.urls")),
    *debug_toolbar_urls(),
]
