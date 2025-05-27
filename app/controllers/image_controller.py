from fastapi import UploadFile, File, HTTPException
from app.services.gcs_service import GCSService
from typing import List

class ImageController:
    def __init__(self):
        self.gcs_service = GCSService()

    def upload_image(self, file: UploadFile) -> str:
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File is not an image.")
        url = self.gcs_service.upload_image(file.file, file.filename)
        return url

    def get_images(self) -> List[str]:
        return self.gcs_service.list_images() 