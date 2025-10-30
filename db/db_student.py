from schemas import StudentBase
from sqlalchemy.orm import Session
from db.models import DbStudent
from fastapi.exceptions import HTTPException
from fastapi import status

# ---------- CREATE STUDENT ----------
def create_student(db: Session, request: StudentBase):
    new_student = DbStudent(
        name=request.name,
        age=request.age,
        address=request.address,
        is_active=request.is_active,
        percentage_range_id=request.percentage_range_id,
        created_by=request.created_id,  # link student to the admin
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


# ---------- GET ALL STUDENTS ----------
def get_all_students(db: Session):
    return db.query(DbStudent).all()

# ---------- GET STUDENT BY ID ----------
def get_student_by_id(db: Session, id: int):
    student = db.query(DbStudent).filter(DbStudent.id == id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {id} not found for"
            
            
            
            
            
        )
    return student





# ---------- UPDATE STUDENT ----------
# ---------- UPDATE STUDENT ----------
def update_student(db: Session, id: int, request: StudentBase, admin_id: int):
    student = db.query(DbStudent).filter(DbStudent.id == id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {id} not found"
        )

    # Only the admin who created the student can update
    if student.created_by != admin_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    # ✅ Correct way: assign values
    student.name = request.name
    student.age = request.age
    student.address = request.address
    student.is_active = request.is_active
    student.percentage_range_id = request.percentage_range_id

    db.commit()
    db.refresh(student)  # optional but good practice
    return {"message": "Student updated successfully"}



# ---------- DELETE STUDENT ----------
def delete_student(db: Session, id: int, admin_id: int):
    student = db.query(DbStudent).filter(DbStudent.id == id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {id} not found"
        )

    # Only the admin who created the student can delete
    if student.created_by != admin_id:
        
        
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}
