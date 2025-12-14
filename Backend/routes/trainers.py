from fastapi import APIRouter, Depends
from database import users_collection
from utils.auth import get_current_user
from bson import ObjectId

router = APIRouter(prefix="/trainers", tags=["Trainers"])

@router.post("/{trainer_id}/follow")
def follow_trainer(trainer_id: str, current_user=Depends(get_current_user)):
    users_collection.update_one(
        {"_id": ObjectId(current_user["_id"])},
        {"$addToSet": {"following": trainer_id}}
    )
    return {"message": "Trainer followed"}

@router.post("/{trainer_id}/unfollow")
def unfollow_trainer(trainer_id: str, current_user=Depends(get_current_user)):
    users_collection.update_one(
        {"_id": ObjectId(current_user["_id"])},
        {"$pull": {"following": trainer_id}}
    )
    return {"message": "Trainer unfollowed"}
