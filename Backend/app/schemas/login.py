from pydantic import BaseModel


class LoginStartRequest(BaseModel):
    username: str
    blinded_password: str


class LoginStartResponse(BaseModel):
    evaluated_password: str
    server_public_key: str
    credential_record: str
    envelope: str


class LoginFinishRequest(BaseModel):
    username: str
    shared_secret: str