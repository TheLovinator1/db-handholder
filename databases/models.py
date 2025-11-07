from typing import TYPE_CHECKING
from typing import ClassVar

from django.db import models

if TYPE_CHECKING:
    from datetime import datetime


class DatabaseInstance(models.Model):
    DB_TYPES: ClassVar[list[tuple[str, str]]] = [
        # SQL Databases
        ("postgresql", "PostgreSQL"),
        ("mysql", "MySQL"),
        ("mariadb", "MariaDB"),
        # Key-value databases
        ("redis", "Redis"),
        ("valkey", "Valkey"),
        # NoSQL Databases
        ("mongodb", "MongoDB"),
    ]
    name: models.CharField[str] = models.CharField(max_length=50, unique=True)
    db_type: models.CharField[str] = models.CharField(max_length=20, choices=DB_TYPES)

    created_at: models.DateTimeField[datetime] = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField[datetime] = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name: str = "Database Instance"
        verbose_name_plural: str = "Database Instances"
        ordering: ClassVar[list[str]] = ["name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.db_type})"
