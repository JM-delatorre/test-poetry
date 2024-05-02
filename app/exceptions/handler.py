from http import HTTPStatus

from app.dto.responses.api_response import ApiResponse

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException


async def validation_request_validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(jsonable_encoder(ApiResponse[str](message="Invalid data", error=jsonable_encoder(exc.errors()), status_code=HTTPStatus.BAD_REQUEST)), status_code=HTTPStatus.BAD_REQUEST)

async def http_error_handler(request: Request, exc: HTTPException):
    return JSONResponse(jsonable_encoder(ApiResponse[str](message=exc.detail, error=[str(exc.detail)], status_code=exc.status_code)), status_code=exc.status_code)
