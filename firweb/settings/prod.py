import os
import io

import environ
from google.cloud import secretmanager
from .common import BASE_DIR

env = environ.Env()
env_file = os.path.join(BASE_DIR, ".env")

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

if os.path.isfile(env_file):
    # Use a local secret file, if provided
    env.read_env(env_file)
else:
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

DATABASES['default']['NAME'] = 'firweb_staging'

print(DATABASES)

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = env.str("GS_BUCKET_NAME")
