# db/db_percentage.py
from sqlalchemy.orm import Session
from db.models import DbPercentageRange
from schemas import PercentageRangeBase

# ✅ Create new percentage range
def create_percentage_range(request: PercentageRangeBase, db: Session):
    new_range = DbPercentageRange(
        percentage_range=request.percentage_range
    )
    db.add(new_range)
    db.commit()
    db.refresh(new_range)
    return new_range

# ✅ Get all percentage ranges
def get_all_percentage_ranges(db: Session):
    return db.query(DbPercentageRange).all()

# ✅ Get percentage range by ID (optional)
def get_percentage_range(id: int, db: Session):
    return db.query(DbPercentageRange).filter(DbPercentageRange.id == id).first()
