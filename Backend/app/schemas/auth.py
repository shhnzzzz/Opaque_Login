from pydantic import BaseModel


class RegisterStartRequest(BaseModel):
    username: str
    email: str
    blinded_password: str


class RegisterStartResponse(BaseModel):
    evaluated_password: str
    server_public_key: str

class RegisterFinishRequest(BaseModel):
    username: str
    email: str
    credential_record: str
    envelope: str
    server_public_key: str