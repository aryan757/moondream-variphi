from pydantic import BaseModel, HttpUrl
from typing import Literal

class CaptionRequest(BaseModel):
    image_url: HttpUrl
    length: Literal['normal', 'long', 'short']

class QueryRequest(BaseModel):
    image_url: HttpUrl
    query: str

class DetectRequest(BaseModel):
    image_url: HttpUrl
    object_to_detect: str

class PointRequest(BaseModel):
    image_url: HttpUrl
    object_to_point: str 