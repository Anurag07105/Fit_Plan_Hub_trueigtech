from fastapi import APIRouter, Depends, HTTPException
from schemas.FitnessPlan import PlancreateSchema, PlanResponse
from database import plans_collection
from utils.auth import get_current_user
from bson import ObjectId

router = APIRouter(prefix="/plans", tags=["Plans"])

@router.post("/", response_model=dict)
def create_plan(plan: PlancreateSchema, current_user=Depends(get_current_user)):
    if current_user["role"] != "trainer":
        raise HTTPException(status_code=403, detail="Only trainers can create plans")

    data = plan.dict()
    data["trainer_id"] = str(current_user["_id"])

    plans_collection.insert_one(data)
    return {"message": "Plan created successfully"}

@router.get("/", response_model=list[PlanResponse])
def list_plans():
    plans = list(plans_collection.find())

    for p in plans:
        p["id"] = str(p["_id"])
        del p["_id"]

    return plans
