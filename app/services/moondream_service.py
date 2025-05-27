import moondream as md
from PIL import Image
import requests
from io import BytesIO
import os
from dotenv import load_dotenv  # type: ignore
load_dotenv()
MOONDRM_API_KEY = os.getenv("MOONDRM_API_KEY")

print("API KEY:", MOONDRM_API_KEY)

model = md.vl(api_key=MOONDRM_API_KEY)

# model = md.vl(api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlfaWQiOiI2YzkyNTVjMy04YTY5LTQyODgtOGMwNi1mNzljNjJlODFjYmMiLCJvcmdfaWQiOiJmeWdKb1ZsS2l6SGF4dGkwTEk4YjFjcUlkV3ZLd3BDUyIsImlhdCI6MTc0ODMyOTkzMCwidmVyIjoxfQ.nmqSfQsExP_yxZ6ezicg1qCb8mSAfQdg5qlCjCDOgug")
# model = md.vl(api_key=os.getenv("MOONDRM_API_KEY"))

# print("API KEY:", os.getenv("MOONDREAM_API_KEY"))

class MoondreamService:
    @staticmethod
    def load_image_from_url(url: str) -> Image.Image:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))

    def caption(self, image_url: str, length: str) -> str:
        img = self.load_image_from_url(image_url)
        return model.caption(img, length=length)["caption"]

    def query(self, image_url: str, query: str) -> str:
        img = self.load_image_from_url(image_url)
        return model.query(img, query)

    def detect(self, image_url: str, object_name: str):
        img = self.load_image_from_url(image_url)
        return model.detect(img, object_name)

    def point(self, image_url: str, object_name: str):
        img = self.load_image_from_url(image_url)
        return model.point(img, object_name) 