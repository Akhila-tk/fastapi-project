from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from db.hash import Hash
from schemas import AdminBase
from db.models import DbAdmin

def create_admin(db: Session, request: AdminBase):
    
   

    # Check if username exists
    admin = db.query(DbAdmin).filter(DbAdmin.username == request.username).first()
    if admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    # Check if email exists
    email = db.query(DbAdmin).filter(DbAdmin.email == request.email).first()
    if email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    # ✅ Create new admin
    new_admin = DbAdmin(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
        
    )

    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

# get admin by ID

def get_admin_by_id(db: Session, id: int):
    admin = db.query(DbAdmin).filter(DbAdmin.id == id).first()
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Admin with id {id} not found'
        )
    return admin


# get admin by username
def get_admin_by_username(db: Session, username: str):
    admin = db.query(DbAdmin).filter(DbAdmin.username == username).first()
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Admin with username {username} not found'
        )
    return admin
