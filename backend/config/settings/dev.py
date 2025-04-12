# backend/config/settings/dev.py
from .base import *

DEBUG = True

# Database (SQLite for development)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Add debug tools
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1"]

# Allow all CORS for development
CORS_ALLOW_ALL_ORIGINS = True