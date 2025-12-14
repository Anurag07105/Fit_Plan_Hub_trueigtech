from fastapi import APIRouter, Depends, HTTPException
from schemas.FitnessPlan import PlancreateSchema
from database import plans_collection 
from utils.auth import get_current_user
from bson.objectid import ObjectId

router = APIRouter(prefix="/trainers", tags=["trainers"])
@router.post("/create_plan")
def create_plan(data: PlancreateSchema, user=Depends(get_current_user)):
    if user["role"] != "trainer":
        raise HTTPException(status_code=403, detail="Only trainers can create plans")
    
    plan = {
        "title": data.title,
        "description": data.description,
        "price": data.price,
        "duration": data.duration,
        "trainer_id": str(user["_id"])
    }
    result = plans_collection.insert_one(plan)
    return {"message": "Plan created successfully", "plan_id": str(result.inserted_id)}

@router.delete("/plans/{plan_id}")
def delete_plan(plan_id: str, user=Depends(get_current_user)):
    plan = plans_collection.find_one({"_id": ObjectId(plan_id)})
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    if plan["trainer_id"] != str(user["_id"]):
        raise HTTPException(status_code=403, detail="Not authorized to delete this plan")
    
    plans_collection.delete_one({"_id": ObjectId(plan_id)})
    return {"message": "Plan deleted successfully"
            }