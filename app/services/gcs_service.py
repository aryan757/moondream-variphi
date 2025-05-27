import os
from google.cloud import storage
from typing import List

GCS_CREDENTIALS = 'service-account-file.json'
BUCKET_NAME = 'moondream-variphi'

class GCSService:
    def __init__(self):
        self.client = storage.Client.from_service_account_json(GCS_CREDENTIALS)
        self.bucket = self.client.bucket(BUCKET_NAME)

    def upload_image(self, file_obj, destination_blob_name: str) -> str:
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_file(file_obj, content_type='image/jpeg')
        return f"https://storage.googleapis.com/{self.bucket.name}/{destination_blob_name}"

    def list_images(self) -> List[str]:
        blobs = self.client.list_blobs(BUCKET_NAME)
        return [blob.public_url for blob in blobs if blob.public_url] 