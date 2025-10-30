# routes/percentage.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas import PercentageRangeBase, PercentageRangeDisplay
from db import db_percentage
from typing import List

router = APIRouter(
    prefix="/percentage",
    tags=["Percentage Range"]
)

# ✅ Create percentage range
@router.post("/", response_model=PercentageRangeDisplay)
def create_percentage_range(request: PercentageRangeBase, db: Session = Depends(get_db)):
    return db_percentage.create_percentage_range(request, db)

# ✅ Get all percentage ranges
@router.get("/", response_model=List[PercentageRangeDisplay])
def get_all_percentage_ranges(db: Session = Depends(get_db)):
    return db_percentage.get_all_percentage_ranges(db)
