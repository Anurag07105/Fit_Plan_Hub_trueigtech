from pydantic import BaseModel , EmailStr

class Signupschema(BaseModel):
    name: str
    email: str
    password: str
    role: str

    class Config:
        extra = "forbid"

class Loginschema(BaseModel):
    email: str
    password: str    

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: str    