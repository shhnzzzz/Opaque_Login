from pydantic import BaseModel


class RegisterStartRequest(BaseModel):
    username: str
    blinded_password: str


class RegisterStartResponse(BaseModel):
    evaluated_password: int