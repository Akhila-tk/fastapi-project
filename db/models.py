from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class DbAdmin(Base):
    __tablename__ = "admin_master"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    students = relationship("DbStudent", back_populates="admin")
    
    
class DbPercentageRange(Base):
    __tablename__ = "percentage_range"

    id = Column(Integer, primary_key=True, index=True)
    percentage_range = Column(String(10), unique=True, nullable=False)

    
    students = relationship("DbStudent", back_populates="percentage_range")
    
    


class DbStudent(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String)
    is_active = Column(Boolean, default=True)

     # Foreign keys
    percentage_range_id = Column(Integer, ForeignKey("percentage_range.id"), nullable=False)
    created_by = Column(Integer, ForeignKey("admin_master.id"))
    # Relationships
    admin = relationship("DbAdmin", back_populates="students")
    percentage_range = relationship("DbPercentageRange", back_populates="students")
