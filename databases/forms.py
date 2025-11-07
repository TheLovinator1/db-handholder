from __future__ import annotations

from typing import TYPE_CHECKING
from typing import ClassVar

from django import forms

from .models import DatabaseInstance

if TYPE_CHECKING:
    from django.forms import Select
    from django.forms import TextInput


class DatabaseInstanceForm(forms.ModelForm):
    class Meta:
        model = DatabaseInstance
        fields: ClassVar[list[str]] = ["name", "db_type"]
        widgets: ClassVar[dict[str, TextInput | Select]] = {
            "name": forms.TextInput(attrs={"placeholder": "e.g. reporting-db", "autofocus": "autofocus"}),
            "db_type": forms.Select(),
        }

    def clean_name(self) -> str:
        name: str = (self.cleaned_data.get("name") or "").strip()
        if not name:
            msg = "Name is required."
            raise forms.ValidationError(msg)
        return name
