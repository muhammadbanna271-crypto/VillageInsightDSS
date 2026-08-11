"""
Django settings for VillageInsight DSS.

Version : 1.0.0
"""

from pathlib import Path
from dotenv import load_dotenv
import os
import dj_database_url
# --------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

load_dotenv(BASE_DIR.parent / ".env")

# --------------------------------------------------
# SECURITY
# --------------------------------------------------

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-change-this-secret-key"
)

# --------------------------------------------------
# CHATBOT (Claude API)
# --------------------------------------------------

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

CHATBOT_MODEL = os.getenv("CHATBOT_MODEL", "claude-sonnet-5")

CHATBOT_MAX_MESSAGES_PER_SESSION = int(
    os.getenv("CHATBOT_MAX_MESSAGES_PER_SESSION", "30")
)

# Lapis pengaman KEDUA di sisi aplikasi (lapis pertama & paling
# kuat tetap monthly spend limit di console.anthropic.com).
# Estimasi biaya per pesan pakai harga STANDAR Sonnet 5 yang
# berlaku mulai 1 Sept 2026 ($3/$15 per juta token), bukan harga
# promo yang sedang berjalan ($2/$10) -- supaya batasnya tetap
# valid dan tidak perlu diubah lagi bulan depan. Angkanya juga
# sengaja dilebihkan dari estimasi rata-rata sebagai margin aman.
CHATBOT_MONTHLY_BUDGET_USD = float(
    os.getenv("CHATBOT_MONTHLY_BUDGET_USD", "10")
)

CHATBOT_ESTIMATED_COST_PER_MESSAGE_USD = float(
    os.getenv("CHATBOT_ESTIMATED_COST_PER_MESSAGE_USD", "0.01")
)

# --------------------------------------------------
# DEEPSEEK (engine kedua, bebas akses tanpa password)
# --------------------------------------------------

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")

DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

# --------------------------------------------------
# Password gate untuk engine Claude (biar pemakaiannya
# dibatasi manual, tidak sembarang orang bisa akses)
# --------------------------------------------------

CHATBOT_CLAUDE_PASSWORD = os.getenv("CHATBOT_CLAUDE_PASSWORD", "")

DEBUG = os.getenv("DEBUG", "True") == "True"
RAILWAY_HOST = os.getenv("RAILWAY_PUBLIC_DOMAIN")
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "127.0.0.1,localhost"
).split(",")

if RAILWAY_HOST:
    ALLOWED_HOSTS.append(RAILWAY_HOST)
# --------------------------------------------------
# APPLICATION DEFINITION
# --------------------------------------------------

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "django_filters",
    "widget_tweaks",
    "django_extensions",
]

LOCAL_APPS = [
    "apps.master",
]

INSTALLED_APPS = [

    # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Local Apps
    "common",
    "apps.master",
    "apps.survey",
    "apps.respondent",
    "apps.response",
    "apps.analytics",
    "apps.dashboard",
    "apps.recommendation.apps.RecommendationConfig",
    "apps.chatbot",

]

# --------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

# --------------------------------------------------
# ROOT URL
# --------------------------------------------------

ROOT_URLCONF = "config.urls"

# --------------------------------------------------
# TEMPLATE
# --------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
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

WSGI_APPLICATION = "config.wsgi.application"

# --------------------------------------------------
# DATABASE
# --------------------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.getenv(
                "DB_ENGINE",
                "django.db.backends.sqlite3"
            ),
            "NAME": os.getenv(
                "DB_NAME",
                BASE_DIR / "db.sqlite3"
            ),
            "USER": os.getenv("DB_USER", ""),
            "PASSWORD": os.getenv("DB_PASSWORD", ""),
            "HOST": os.getenv("DB_HOST", ""),
            "PORT": os.getenv("DB_PORT", ""),
        }
    }

# --------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# --------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Jakarta"

USE_I18N = True

USE_TZ = True

# --------------------------------------------------
# STATIC
# --------------------------------------------------

STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# --------------------------------------------------
# MEDIA
# --------------------------------------------------

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

# --------------------------------------------------
# DEFAULT PRIMARY KEY
# --------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------------------------------
# CRISPY FORMS
# --------------------------------------------------

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

# --------------------------------------------------
# LOGIN
# --------------------------------------------------

LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "dashboard:dashboard"

LOGOUT_REDIRECT_URL = "login"

# --------------------------------------------------
# LOGGING
# --------------------------------------------------

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
}

STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

CSRF_TRUSTED_ORIGINS = [
    "trip1.up.railway.app",
]

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
# --------------------------------------------------
# END
# --------------------------------------------------