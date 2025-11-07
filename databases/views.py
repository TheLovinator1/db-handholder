from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import DatabaseInstanceForm
from .models import DatabaseInstance

if TYPE_CHECKING:
    from django.db.models.manager import BaseManager
    from django.http import HttpRequest
    from django.http import HttpResponse


# databases/add/
def add_database(request: HttpRequest) -> HttpResponse:
    """Create a new DatabaseInstance via a plain HTML form.

    - GET: render the empty form
    - POST: validate and save; on success, redirect back to the form with a success message

    Returns:
            HttpResponse: The rendered form page or a redirect on successful creation.
    """
    if request.method == "POST":
        form = DatabaseInstanceForm(request.POST)
        if form.is_valid():
            instance: DatabaseInstance = form.save()
            messages.success(request, f"Database '{instance.name}' ({instance.db_type}) created successfully.")
            return redirect("databases")
    else:
        form = DatabaseInstanceForm()

    return render(request, template_name="databases/database_form.html", context={"form": form})


# /databases
def list_databases(request: HttpRequest) -> HttpResponse:
    """Render a plain HTML page listing all DatabaseInstance rows.

    Uses only server-rendered HTML (no CSS/JS). If there are no databases,
    the page displays a friendly empty-state message.

    Returns:
        HttpResponse: The rendered list page.
    """
    databases: BaseManager[DatabaseInstance] = DatabaseInstance.objects.all()
    context: dict[str, BaseManager[DatabaseInstance]] = {"databases": databases}
    return render(request, template_name="databases/database_list.html", context=context)
