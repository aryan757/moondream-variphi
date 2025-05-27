from fastapi import APIRouter, UploadFile, File
from app.controllers.image_controller import ImageController
from typing import List

router = APIRouter()
controller = ImageController()

@router.post("/upload")
def upload_image(file: UploadFile = File(...)):
    url = controller.upload_image(file)
    return {"url": url}

@router.get("/get_images", response_model=List[str])
def get_images():
    return controller.get_images() 