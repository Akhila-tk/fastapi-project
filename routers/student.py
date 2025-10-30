from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from schemas import StudentBase, StudentDisplay, AdminAuth
from db.database import get_db
from db import db_student
from authentication.oauth2 import get_current_admin

router = APIRouter(
    prefix='/student',
    tags=['student']
)

@router.post('', response_model=StudentDisplay)
def create_student(
    request: StudentBase,
    db: Session = Depends(get_db),
    current_admin: AdminAuth = Depends(get_current_admin)
):

    return db_student.create_student(db, request)

# ---------- GET ALL STUDENTS ----------


@router.get('/all', response_model=List[StudentDisplay])
def get_students(db: Session = Depends(get_db)):
    return db_student.get_all_students(db)

# ---------- GET ONE STUDENT ----------
@router.get('/{id}', response_model=StudentDisplay)
def get_student(id: int, db: Session = Depends(get_db)):
    return db_student.get_student_by_id(db, id)



# ---------- UPDATE STUDENT ----------
@router.put('/update/{id}')
def update_student(
    id: int,
    request: StudentBase,
    db: Session = Depends(get_db),
    current_admin: AdminAuth = Depends(get_current_admin)
):
    return db_student.update_student(db, id, request, current_admin.id)


# ---------- DELETE STUDENT ----------
@router.delete('/delete/{id}')
def delete_student(
    id: int,
    db: Session = Depends(get_db),
    current_admin: AdminAuth = Depends(get_current_admin)
):
    return db_student.delete_student(db, id, current_admin.id)
