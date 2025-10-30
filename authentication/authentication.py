from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.database import get_db
from db.models import DbAdmin
from db.hash import Hash
from authentication import oauth2

router = APIRouter(
    tags=['authentication']
)

@router.post('/login', summary="User Login", description="Login with username and password")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    admin = db.query(DbAdmin).filter(DbAdmin.username == request.username).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials')
    if not Hash.verify(request.password, admin.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')

    access_token = oauth2.create_access_token(data={'sub': admin.username})

    return {
    'access_token': access_token,
    'token_type': 'bearer',
    'admin_id': admin.id,
    'username': admin.username
}
