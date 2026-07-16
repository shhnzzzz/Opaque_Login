from fastapi import APIRouter

from app.schemas.opaque import (
    RegisterStartRequest,
    RegisterStartResponse,
)

from app.opaque.oprf import evaluate

router = APIRouter(
    prefix="/opaque",
    tags=["OPAQUE"],
)


@router.post(
    "/register/start",
    response_model=RegisterStartResponse,
)
async def register_start(data: RegisterStartRequest):

    evaluated = evaluate(int(data.blinded_password))

    return RegisterStartResponse(
        evaluated_password=evaluated
    )