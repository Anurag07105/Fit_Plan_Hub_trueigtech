from fastapi import Depends, HTTPException, APIRouter
from database import follows_collection, users_collection, subscribtions_collection, plans_collection
from utils.auth import get_current_user

router = APIRouter(prefix="/feed", tags=["feed"])
@router.get("/")
def personalized_feed(user=Depends(get_current_user)):
    followed = follows_collection.find({"user_id": user["id"]})
    trainer_ids = [f["trainer_id"] for f in followed]

    plans = plans_collection.find({"trainer_id": {"$in": trainer_ids}})
    purchased = {
        s["plan_id"]
        for s in subscribtions_collection.find({"user_id": user["id"]})
    }

    feed = []
    for p in plans:
        feed.append({
            "title": p["title"],
            "trainer_id": p["trainer_id"],
            "purchased": str(p["_id"]) in purchased
        })
    return feed
            