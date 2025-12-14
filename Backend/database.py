from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
users_collection = db.users
plans_collection = db.plans
subscribtions_collection = db.subscribtions
follows_collection = db.follows