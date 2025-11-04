import os
from pathlib import Path

import django_stubs_ext
from platformdirs import user_data_dir

django_stubs_ext.monkeypatch()

BASE_DIR: Path = Path(__file__).resolve().parent.parent
DATA_DIR: Path = Path(user_data_dir(appname="db_handholder", appauthor="TheLovinator", roaming=True, ensure_exists=True))

INTERNAL_IPS: list[str] = ["127.0.0.1"]
SECRET_KEY: str = os.getenv(key="DJANGO_SECRET_KEY", default="django-insecure-placeholder-key")
DEBUG: bool = os.getenv(key="DJANGO_DEBUG", default="True") == "True"

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if not DEBUG:
    ALLOWED_HOSTS: list[str] = os.getenv(key="DJANGO_ALLOWED_HOSTS", default="").split(",")

TIME_ZONE = "UTC"
STATIC_URL = "static/"

SITE_ID: int = 1

INSTALLED_APPS: list[str] = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_browser_reload",
    "django_watchfiles",
    "debug_toolbar",
    "django_minify_html",
]

MIDDLEWARE: list[str] = [
    "django_minify_html.middleware.MinifyHtmlMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]


TEMPLATES: list[dict[str, str | bool | list[str] | dict[str, list[str]]]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# TODO(TheLovinator): Should we autocreate a Postgresql database on startup based on env vars?
DATABASES: dict[str, dict[str, str | Path | dict[str, str]]] = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DATA_DIR / "db.sqlite3",
        "OPTIONS": {
            "init_command": (
                "PRAGMA foreign_keys=ON;"
                "PRAGMA journal_mode = WAL;"
                "PRAGMA synchronous = NORMAL;"
                "PRAGMA busy_timeout = 5000;"
                "PRAGMA temp_store = MEMORY;"
                "PRAGMA mmap_size = 134217728;"
                "PRAGMA journal_size_limit = 67108864;"
                "PRAGMA cache_size = 2000;"
            ),
            "transaction_mode": "IMMEDIATE",
        },
    },
}
