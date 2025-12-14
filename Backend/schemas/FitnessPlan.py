from pydantic import BaseModel

class PlancreateSchema(BaseModel):
    title: str
    description: str
    price: float
    duration: int

class PlanResponse(BaseModel):
    id: str
    title: str
    description: str
    price: float
    preview_content: str
    trainer_id: str