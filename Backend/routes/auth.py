from fastapi import APIRouter, HTTPException
from schemas.user import UserSignup, UserLogin, UserResponse
from database import users_collection
from utils.security import hash_password, verify_password
from utils.auth import create_token
from bson import ObjectId

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup", response_model=dict)
def signup(data: UserSignup):
    if users_collection.find_one({"email": data.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    user = {
        "name": data.name,
        "email": data.email,
        "hashed_password": hash_password(data.password),
        "role": data.role,
        "is_active": True
    }

    users_collection.insert_one(user)
    return {"message": "User created successfully"}

@router.post("/login", response_model=dict)
def login(data: UserLogin):
    user = users_collection.find_one({"email": data.email})

    if not user or not verify_password(data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(str(user["_id"]))

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "role": user["role"]
        }
    }
