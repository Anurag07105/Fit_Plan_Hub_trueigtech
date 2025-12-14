from fastapi import FastAPI
from routes import auth, plans, feed, trainers
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI(title="FitPlanHub")
app.include_router(auth.router)
app.include_router(plans.router)
app.include_router(feed.router)
app.include_router(trainers.router)  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)