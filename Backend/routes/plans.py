from fastapi import APIRouter , Depends, HTTPException 
from database import plans_collection, subscribtions_collection
from utils.auth import get_current_user
from bson.objectid import ObjectId

router = APIRouter(prefix= "/plans",tags=["plans"])
@router.get("/")
def view_plans():
    plans = []
    for plan in plans_collection.find():
        plans.append({
            "id": str(plan-["_id"]),
            "title": plan["title"],
            "price": plan["price"],
            "trainer_id": plan["trainer_id"]
        })
    return {"plans": plans}

router.post("/{plan_id}/subscribe")
def subscribe_plan(plan_id: str, user=Depends(get_current_user)):
    plan = plans_collection.find_one({"_id": ObjectId(plan_id)})
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    
    existing_subscription = subscribtions_collection.find_one({
        "user_id": str(user["_id"]),
        "plan_id": plan_id
    })
    if existing_subscription:
        raise HTTPException(status_code=400, detail="Already subscribed to this plan")
    
    subscription = {
        "user_id": str(user["_id"]),
        "plan_id": plan_id
    }
    subscribtions_collection.insert_one(subscription)
    return {"message": "Subscribed to plan successfully"}
