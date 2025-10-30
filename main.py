from fastapi import FastAPI
from db import models, database
from routers import admin,percentage,student
from authentication import authentication
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(admin.router)
app.include_router(percentage.router)
app.include_router(student.router)



@app.get("/")
def root():
    return {"message": "Welcome to FastAPI + React Auth System 🚀"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)
