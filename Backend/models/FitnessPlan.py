from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId

class FitnessPlan(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    title: str
    description: str
    price: float = 0.0
    preview_content: str
    full_content: Optional[str] = None
    trainer_id: str
    tags: List[str] = []
    is_published: bool = True

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
