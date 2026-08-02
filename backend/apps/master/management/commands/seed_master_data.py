"""
Management command: seed_master_data

Mengisi master data yang WAJIB ada sebelum 1.152 respons bisa
diimpor lewat /response/import/:
  - 1 District placeholder ("Kota Batu") -- ganti manual nanti
    kalau butuh kecamatan asli per desa (Batu/Bumiaji/Junrejo)
  - 24 Village (persis VILLAGE_ID_MAP di bulk_import_service.py)
  - 11 Variable (X1-X5, Y1-Y6)
  - 88 Indicator (linked ke Variable masing-masing)
  - 88 Questionnaire (1 per Indicator, answer_type="likert",
    karena semua jawaban di data respons berskala 1-5)
  - 1 Survey ("Survei Desa Wisata Kota Batu 2026") -- dipakai
    saat mengisi form impor di /response/import/

Aman dijalankan berkali-kali: pakai get_or_create, tidak akan
membuat duplikat kalau dijalankan ulang.

CARA PAKAI:
1. Salin file ini ke:
   backend/apps/master/management/commands/seed_master_data.py
   (buat folder management/ dan commands/ kalau belum ada,
   masing-masing perlu file __init__.py kosong di dalamnya)
2. Salin seed_master_data.json ke folder backend/ (sejajar manage.py)
3. Jalankan: python manage.py seed_master_data
"""

import json
from pathlib import Path

from django.core.management.base import BaseCommand
from django.conf import settings

from apps.master.models import District, Village, Variable, Indicator, Questionnaire
from apps.survey.models import Survey


class Command(BaseCommand):
    help = "Isi master data (district, village, variable, indicator, questionnaire, survey) dari seed_master_data.json"

    def handle(self, *args, **options):

        seed_path = Path(settings.BASE_DIR) / "seed_master_data.json"

        if not seed_path.exists():
            self.stderr.write(
                self.style.ERROR(
                    f"Tidak ketemu {seed_path}. "
                    "Pastikan seed_master_data.json ada di folder backend/."
                )
            )
            return

        with open(seed_path, encoding="utf-8") as f:
            seed = json.load(f)

        # --- District (placeholder) ---
        district, _ = District.objects.get_or_create(
            code="BATU",
            defaults={"name": "Kota Batu"},
        )
        self.stdout.write(self.style.SUCCESS("District siap: Kota Batu"))

        # --- Village (24) ---
        village_count = 0
        for v in seed["villages"]:
            _, created = Village.objects.get_or_create(
                code=f"DS{v['id']:02d}",
                defaults={
                    "name": v["name"],
                    "district": district,
                },
            )
            village_count += 1
        self.stdout.write(self.style.SUCCESS(f"Village siap: {village_count} desa"))

        # --- Variable (11) ---
        variable_objs = {}
        for v in seed["variables"]:
            obj, _ = Variable.objects.get_or_create(
                code=v["code"],
                defaults={"name": v["name"]},
            )
            variable_objs[v["code"]] = obj
        self.stdout.write(self.style.SUCCESS(f"Variable siap: {len(variable_objs)} variabel"))

        # --- Indicator + Questionnaire (88) ---
        indicator_count = 0
        questionnaire_count = 0
        for ind in seed["indicators"]:
            variable = variable_objs.get(ind["variable_code"])
            if variable is None:
                self.stderr.write(
                    self.style.WARNING(
                        f"Variable {ind['variable_code']} tidak ketemu, indikator {ind['code']} dilewati"
                    )
                )
                continue

            indicator_obj, _ = Indicator.objects.get_or_create(
                code=ind["code"],
                defaults={
                    "name": ind["name"][:100],
                    "description": ind["description"],
                    "variable": variable,
                },
            )
            indicator_count += 1

            _, q_created = Questionnaire.objects.get_or_create(
                indicator=indicator_obj,
                defaults={
                    "question": ind["description"],
                    "answer_type": "likert",
                    "question_order": 1,
                },
            )
            questionnaire_count += 1

        self.stdout.write(self.style.SUCCESS(f"Indicator siap: {indicator_count} indikator"))
        self.stdout.write(self.style.SUCCESS(f"Questionnaire siap: {questionnaire_count} pertanyaan"))

        # --- Survey (1) ---
        survey, _ = Survey.objects.get_or_create(
            name="Survei Desa Wisata Kota Batu 2026",
            defaults={
                "description": "Survei 1.152 responden, 24 desa wisata Kota Batu",
                "start_date": "2026-01-01",
                "end_date": "2026-12-31",
                "is_active": True,
            },
        )
        self.stdout.write(self.style.SUCCESS(f"Survey siap: {survey.name}"))

        self.stdout.write(self.style.SUCCESS("\nSelesai. Master data sudah lengkap, siap untuk impor respons."))
