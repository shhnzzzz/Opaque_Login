from fastapi import APIRouter
from app.schemas.auth import (
    RegisterStartRequest,
    RegisterStartResponse,
    RegisterFinishRequest,
)
from app.database.database import db

from app.services.auth_services import (
    start_registration,
    finish_registration
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register/start",
    response_model=RegisterStartResponse
)
async def register_start(data: RegisterStartRequest):

    result = await start_registration(data)

    return RegisterStartResponse(**result)
async def register_start(data: RegisterStartRequest):

    # TODO: OPRF Evaluation

    return RegisterStartResponse(
        server_public_key="temp_server_key",
        evaluated_password="123456789"
    )


@router.post("/register/finish")
async def register_finish(data: RegisterFinishRequest):

    return await finish_registration(
        data,
        db
    )

async def register_finish(data: RegisterFinishRequest):

    # TODO: Save credential record

    return {
        "success": True,
        "message": "Registration completed."
    }