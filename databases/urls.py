from typing import TYPE_CHECKING

from django.urls import path

from . import views

if TYPE_CHECKING:
    from django.urls.resolvers import URLPattern

urlpatterns: list[URLPattern] = [
    path(route="databases", view=views.list_databases, name="databases"),
    path(route="databases/add/", view=views.add_database, name="database_add"),
]
