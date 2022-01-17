import os
import io

import environ  # type: ignore
from google.cloud import secretmanager
from google.cloud.secretmanager_v1 import SecretManagerServiceClient

from .common import BASE_DIR

# Imports the Cloud Logging client library
import google.cloud.logging

# Instantiates a client
client = google.cloud.logging.Client()

# Retrieves a Cloud Logging handler based on the environment
# you're running in and integrates the handler with the
# Python logging module. By default this captures all logs
# at INFO level and higher
client.setup_logging()

env = environ.Env()
env_file = os.path.join(BASE_DIR, ".env")

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

if os.path.isfile(env_file):
    # Use a local secret file, if provided
    env.read_env(env_file)
else:
    secret_client = secretmanager.SecretManagerServiceClient()
    settings_name = os.environ.get("SETTINGS_NAME", "django_settings")
    name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
    payload = secret_client.access_secret_version(name=name).payload.data.decode(
        "UTF-8"
    )

    env.read_env(io.StringIO(payload))

DEBUG = False

SECRET_KEY = env("SECRET_KEY")

DATABASES = {
    "default": env.db(),
}

# temporary fix for django-environ bug
# see https://github.com/joke2k/django-environ/issues/294
if "/" in DATABASES["default"]["NAME"]:
    DATABASES["default"]["HOST"], DATABASES["default"]["NAME"] = DATABASES["default"][
        "NAME"
    ].rsplit("/", 1)

if os.getenv("USE_CLOUD_SQL_AUTH_PROXY", None):
    DATABASES["default"]["HOST"] = "127.0.0.1"
    DATABASES["default"]["PORT"] = 5432

DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_BUCKET_NAME = env.str("GS_BUCKET_NAME")
GS_QUERYSTRING_AUTH = False

DJANGOCMS_GOOGLEMAP_API_KEY = env.str("GMAPS_API")

# ONLY safe if deploying through GAE. If deploying elsewhere, this must be modified
ALLOWED_HOSTS = ["*"]

GOOGLE_MEASUREMENT_ID = env.str("GOOGLE_MEASUREMENT_ID", None)
