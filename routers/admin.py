

from fastapi import APIRouter, Depends
from schemas import AdminDisplay, AdminBase
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_adminregister

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)

@router.post('', response_model=AdminDisplay)
def create_admin(request: AdminBase, db: Session = Depends(get_db)):
    return db_adminregister.create_admin(db, request)

# ✅ Get user by ID
@router.get("/{id}", response_model=AdminDisplay)
def get_admin(id: int, db: Session = Depends(get_db)):
    return db_adminregister.get_admin_by_id(db, id)