# db-handholder

Simplify database management. Django web UI for automated database provisioning, backups, and security on any infrastructure.

## TL;DR - Quick Commands

```powershell
uv sync

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Add a new database (HTML-only form)

- URL: `/databases/add/`
- Description: Plain HTML form (no JavaScript) to create a new `DatabaseInstance` with a unique `name` and a `db_type` choice.
- On success: You will be redirected back to the form and see a green success message.

Fields:

- Name (text)
- Database type (select: PostgreSQL, MySQL, MariaDB, Redis, Valkey, MongoDB)

This feature is implemented in:

- `databases/forms.py` — `DatabaseInstanceForm`
- `databases/views.py` — `add_database` view
- `databases/urls.py` — route `databases/add/`
- `databases/templates/databases/database_form.html` — plain HTML template
