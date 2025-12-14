from fastapi import APIRouter, HTTPException
from schemas.user import Signupschema, Loginschema
from utils.security import hash_password, verify_password
from utils.auth import create_token
from database import users_collection

router = APIRouter(prefix="/auth", tags=["auth"])   

@router.post("/signup")
def signup(data: Signupschema):
    if users_collection.find_one({"email": data.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    

    user = {
        "name": data.name,
        "email": data.email,
        "password": hash_password(data.password),
        "role": data.role
    }
    users_collection.insert_one(user)
    return {"message": "User created successfully"}

@router.post("/login")
def login(data: Loginschema):
    user = users_collection.find_one({"email": data.email})
    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid Credentils")
    
    token = create_token(str(user["_id"]))
    return{"access_token": token, "token_type": "bearer"}
