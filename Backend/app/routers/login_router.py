from fastapi import APIRouter, HTTPException

from app.database.database import db

from app.schemas.login import (
    LoginStartRequest,
    LoginStartResponse,
    LoginFinishRequest
)

from app.services.login_service import (
    login_start,
    login_finish
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login/start",
    response_model=LoginStartResponse
)
async def start(data: LoginStartRequest):

    result = await login_start(data, db)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return result


@router.post("/login/finish")
async def finish(data: LoginFinishRequest):

    return await login_finish(
        data,
        db
    )