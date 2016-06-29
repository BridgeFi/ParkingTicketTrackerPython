import config
from gcloud import storage


def get_storage_client():
    return storage.Client(
        project=config.CLOUD_PROJECT_ID
    )


def get_bucket():
    client = get_storage_client()
    bucket = client.get_bucket(config.CLOUD_BUCKET_STORAGE)
    return bucket
