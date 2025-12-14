from fastapi import APIRouter, Depends
from database import plans_collection
from utils.auth import get_current_user

router = APIRouter(prefix="/feed", tags=["Feed"])

@router.get("/")
def get_feed(current_user=Depends(get_current_user)):
    followed_trainers = current_user.get("following", [])
    plans = list(plans_collection.find({"trainer_id": {"$in": followed_trainers}}))

    for p in plans:
        p["id"] = str(p["_id"])
        del p["_id"]

    return plans
