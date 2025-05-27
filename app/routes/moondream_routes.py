from fastapi import APIRouter
from app.controllers.moondream_controller import MoondreamController
from app.dto.image_dto import CaptionRequest, QueryRequest, DetectRequest, PointRequest

router = APIRouter()
controller = MoondreamController()

@router.post("/caption")
def generate_caption(request: CaptionRequest):
    result = controller.caption(request.image_url, request.length)
    return {"caption": result}

@router.post("/query")
def answer_query(request: QueryRequest):
    result = controller.query(request.image_url, request.query)
    return {"answer": result}

@router.post("/detect")
def detect_object(request: DetectRequest):
    result = controller.detect(request.image_url, request.object_to_detect)
    return result

@router.post("/point")
def point_object(request: PointRequest):
    result = controller.point(request.image_url, request.object_to_point)
    return result 