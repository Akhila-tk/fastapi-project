
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_adminregister
 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
 
SECRET_KEY = 'ec5383848f4237282f407affd38b445399a83092cc9c9dad6f6af4e2f1114d8c'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 1440  # 24 hours
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_admin(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    admin = db_adminregister.get_admin_by_username(db, username=username)
    if admin is None:
        raise credentials_exception
    return admin
