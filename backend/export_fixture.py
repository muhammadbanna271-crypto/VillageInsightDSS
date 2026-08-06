import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.core.management import call_command

with open("initial_data.json", "w", encoding="utf-8") as f:
    call_command(
        "dumpdata",
        exclude=[
            "contenttypes",
            "auth.permission",
            "admin.logentry",
            "sessions",
        ],
        indent=2,
        stdout=f,
    )

print("✅ initial_data.json berhasil dibuat.")