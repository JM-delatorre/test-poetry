import logging.config

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from starlette.exceptions import HTTPException

from .controllers import seeder_controller
from .exceptions.handler import (http_error_handler, validation_request_validation_error_handler)

app = FastAPI(title="Seeders")

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app.add_exception_handler(
    exc_class_or_status_code=RequestValidationError, handler=validation_request_validation_error_handler)

app.add_exception_handler(
    exc_class_or_status_code=HTTPException, handler=http_error_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(seeder_controller.router, prefix="/v1/seeder", tags=["Seeder"])


handler = Mangum(app)
