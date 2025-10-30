# from passlib.context import CryptContext

# pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated = "auto")


# class Hash:
#     def bcrypt(password:str):
#         return pwd_cxt.hash(password)
    
#     def verify(plain_password,hashed_password):
#         return pwd_cxt.verify(plain_password,hashed_password)
    
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["argon2"], deprecated="auto")

class Hash:
    @staticmethod
    def bcrypt(password: str) -> str:
        return pwd_cxt.hash(str(password).strip())
    
    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        return pwd_cxt.verify(str(plain_password).strip(), hashed_password)



