from .base import *
import dj_database_url

DEBUG = False

# Database (PostgreSQL in production)
DATABASES = {
    "default": dj_database_url.parse(os.getenv("DATABASE_URL")),
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Static files via CDN/Whitenoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"