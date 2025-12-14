from pydantic import BaseModel

class PlancreateSchema(BaseModel):
    title: str
    description: str
    price: float
    duration: int