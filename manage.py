#!/usr/bin/env python
import os
import sys


def main() -> None:
    """Run administrative tasks.

    Raises:
        ImportError: If Django is not installed or cannot be imported.
    """
    os.environ.setdefault(key="DJANGO_SETTINGS_MODULE", value="config.settings")
    try:
        from django.core.management import execute_from_command_line  # noqa: PLC0415
    except ImportError as exc:
        msg = "Couldn't import Django. Did you forget to run 'uv sync'?"
        raise ImportError(msg) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
