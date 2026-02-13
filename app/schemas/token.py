from pydantic import BaseModel

class TokenResponce(BaseModel):
    access_token: str
    refresh_token: str
    token_type: "bearer"

class RefreshTokenRequest(BaseModel):
    refresh_token: str

    
