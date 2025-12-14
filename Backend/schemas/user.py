from pydantic import BaseModel

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