from pydantic import BaseModel
from typing import Optional


class AdminBase(BaseModel):
    username: str
    email: str
    # password:str
    password: str  


class AdminDisplay(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True
        
class PercentageRangeBase(BaseModel):
    percentage_range: str
    
class PercentageRangeDisplay(BaseModel):
    id: int
    percentage_range: str

    class Config:
        from_attributes = True



class StudentBase(BaseModel):
    name: str
    age: int
    address: Optional[str] = None
    is_active: bool = True
    percentage_range_id: int
    created_id: int  # admin ID
    
    
    
class Admin(BaseModel):
        id:int
        username: str

        class Config:
            from_attributes = True
   


class StudentDisplay(BaseModel):
    id: int
    name: str
    age: int
    address: Optional[str] = None
    is_active: bool
    percentage_range: PercentageRangeDisplay
    admin: Admin  # shows which admin added this student

    # class Config:
    #     from_attributes = True


class AdminAuth(BaseModel):
    id:int
    username:str
    email:str