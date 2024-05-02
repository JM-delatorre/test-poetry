from http import HTTPStatus
from fastapi import APIRouter
from app.dto.requests.seeder_request_dto import SeederRequestDTO
from app.dto.responses.seeder_response_dto import SeederResponsetDTO
from app.dto.responses.api_response import ApiResponse
from app.services.seeder_service import SeederService

router = APIRouter()

@router.get("/", response_model=ApiResponse[str])
async def list() -> ApiResponse[None]:
    _service = SeederService()
    response = _service.list()
    return ApiResponse[str](data=response, status_code=HTTPStatus.CREATED, message="Seeds retrieved successfully.") 

@router.post("/", status_code=HTTPStatus.CREATED, response_model=ApiResponse[None])
async def save(seeder_request: SeederRequestDTO) -> ApiResponse[None]:
    _service = SeederService()
    _service.save(seeder_request)
    return ApiResponse[None](status_code=HTTPStatus.CREATED, message="Seeds saved successfully.") 

@router.put("/", response_model=ApiResponse[None])
async def update(seeder_request: SeederRequestDTO) -> ApiResponse[None]:
    _service = SeederService()
    _service.update(seeder_request)
    return ApiResponse[None](status_code=HTTPStatus.CREATED, message="Seeds updated successfully.") 
