import os
import io

import environ
from google.cloud import secretmanager

env = environ.Env()

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

client = secretmanager.SecretManagerServiceClient()
settings_name = os.environ.get("SETTINGS_NAME", "django_settings")
name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")

env.read_env(io.StringIO(payload))

DEBUG = False

SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': env.db(),
}

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = env.str("gs_bucket")
