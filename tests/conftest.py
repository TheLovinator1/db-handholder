import os

# Ensure Django settings are configured when running pytest even without pytest-django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

try:
    import django

    django.setup()
except Exception:
    # If pytest-django is present, settings may already be configured; ignore errors
    pass
