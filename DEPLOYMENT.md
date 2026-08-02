# Deployment Guide

Panduan menjalankan VillageInsight DSS di server (VPS) memakai Docker
Compose -- Django + Gunicorn di belakang Nginx, dengan PostgreSQL.

## 1. Prasyarat di server

- Docker Engine + Docker Compose plugin sudah terpasang
- Port 80 terbuka di firewall
- (opsional, disarankan) domain yang sudah diarahkan ke IP server

## 2. Menyalin proyek ke server

```bash
git clone https://github.com/<owner>/VillageInsightDSS.git
cd VillageInsightDSS
```

## 3. Menyiapkan environment variables

```bash
cp .env.production.example .env
nano .env   # isi SECRET_KEY, DB_PASSWORD, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS
```

Generate `SECRET_KEY` yang aman:

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 4. Build dan jalankan

```bash
docker compose up -d --build
```

Ini otomatis: menunggu database siap, menjalankan migrasi, mengumpulkan
static files, lalu menyalakan Gunicorn di belakang Nginx (lihat
`entrypoint.sh`).

## 5. Setup pertama kali

```bash
docker compose exec web python manage.py createsuperuser
```

Lalu isi master data (village, variable, indicator, questionnaire,
cluster) lewat `/admin/` atau halaman master data.

## 6. Cek statusnya

```bash
docker compose ps
docker compose logs -f web
```

Akses lewat `http://<domain-atau-ip-server>/`.

## 7. Update ke versi terbaru

```bash
git pull
docker compose up -d --build
```

## 8. Backup database

```bash
docker compose exec db pg_dump -U villageinsight villageinsight_dss > backup.sql
```

## 9. HTTPS (belum termasuk, langkah lanjutan)

Konfigurasi `nginx/nginx.conf` di sini masih HTTP polos. Untuk HTTPS,
langkah paling praktis: pasang Certbot (Let's Encrypt) di server,
lalu tambahkan blok `listen 443 ssl` ke `nginx/nginx.conf` sesuai
domain yang dipakai. Ini sengaja belum di-hardcode karena tergantung
domain yang kamu pakai.

## Known limitations

- Belum ada CI/CD otomatis -- deploy ulang masih manual (`git pull`
  + `docker compose up -d --build`)
- Belum ada automated backup terjadwal untuk database
- HTTPS/Certbot belum otomatis, lihat poin 9
