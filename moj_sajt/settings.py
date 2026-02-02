"""
Django settings for moj_sajt project.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
#  SECURITY / ENV
# =========================
# Na Renderu možeš da dodaš env var SECRET_KEY,
# ali da ti radi odmah, ostavljamo fallback:
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-o^76iid!l!@_itvklu%4w0)g0r686x21*vs04@eqp*w#0401g_"
)

# DEBUG: lokalno True, na Renderu postavi DEBUG=0 ili DEBUG=False u env var
DEBUG = os.getenv("DEBUG", "True").lower() in ("1", "true", "yes", "y")

# Render domen + lokalno
ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "mileninikolaci-web.onrender.com",
]

# Ako budeš kupila domen kasnije, dodaš ga ovde, npr:
# "mileninikolaci.rs",
# "www.mileninikolaci.rs",

# Da ne pukne CSRF kad budeš imala formu / admin / bilo šta POST:
CSRF_TRUSTED_ORIGINS = [
    "https://mileninikolaci-web.onrender.com",
]
# (kad dodaš domen, dodaš i njega ovde)

# =========================
#  APPS
# =========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "kolaci",
]

# =========================
#  MIDDLEWARE
#  (SecurityMiddleware NE duplirati)
#  WhiteNoise ide odmah posle SecurityMiddleware
# =========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "moj_sajt.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # ako ikad budeš imala global templates folder, dodaj BASE_DIR / "templates"
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "moj_sajt.wsgi.application"

# =========================
#  DATABASE
# =========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# =========================
#  PASSWORD VALIDATION
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# =========================
#  I18N
# =========================
LANGUAGE_CODE = "sr"
TIME_ZONE = "Europe/Belgrade"
USE_I18N = True
USE_TZ = True

# =========================
#  STATIC FILES (WhiteNoise)
# =========================
STATIC_URL = "static/"

# Render/production: collectstatic ide ovde
STATIC_ROOT = BASE_DIR / "staticfiles"

# Lokalno: gde su ti slike/css (ti već imaš kolaci/static)
STATICFILES_DIRS = [
    BASE_DIR / "kolaci" / "static",
]

# WhiteNoise optimizacija
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# =========================
#  DEFAULT PK
# =========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
