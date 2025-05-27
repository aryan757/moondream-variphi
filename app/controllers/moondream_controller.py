from fastapi import HTTPException
from app.services.moondream_service import MoondreamService
from app.services.gcs_service import GCSService
from PIL import ImageDraw
from io import BytesIO
import requests

class MoondreamController:
    def __init__(self):
        self.moondream_service = MoondreamService()
        self.gcs_service = GCSService()

    def caption(self, image_url: str, length: str):
        return self.moondream_service.caption(image_url, length)

    def query(self, image_url: str, query: str):
        return self.moondream_service.query(image_url, query)

    def detect(self, image_url: str, object_name: str):
        img = self.moondream_service.load_image_from_url(image_url)
        w, h = img.size
        result = self.moondream_service.detect(image_url, object_name)
        boxes = result['objects']
        ov = img.copy()
        d = ImageDraw.Draw(ov)
        for b in boxes:
            d.rectangle([
                int(b['x_min'] * w),
                int(b['y_min'] * h),
                int(b['x_max'] * w),
                int(b['y_max'] * h)
            ], outline='red', width=3)
        buf = BytesIO()
        ov.save(buf, format='JPEG')
        buf.seek(0)
        filename = f"detected_{object_name}.jpg"
        url = self.gcs_service.upload_image(buf, filename)
        return {"detected_image_url": url, "boxes": boxes}

    def point(self, image_url: str, object_name: str):
        img = self.moondream_service.load_image_from_url(image_url)
        w, h = img.size
        result = self.moondream_service.point(image_url, object_name)
        points = result['points']
        ov = img.copy()
        d = ImageDraw.Draw(ov)
        for p in points:
            r = 4
            d.ellipse([
                int(p['x'] * w) - r, int(p['y'] * h) - r,
                int(p['x'] * w) + r, int(p['y'] * h) + r
            ], fill='blue')
        buf = BytesIO()
        ov.save(buf, format='JPEG')
        buf.seek(0)
        filename = f"points_{object_name}.jpg"
        url = self.gcs_service.upload_image(buf, filename)
        return {"points_image_url": url, "points": points} 