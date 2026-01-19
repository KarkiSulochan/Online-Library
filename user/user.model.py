from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum 
from passlib.hash import bcrypt

Base = declarative_base() #base class for sql alchemy models

#Enum for user roles
class UserRole(enum.Enum):
    ADMIN = "admin"
    USER = "user"

    class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        
        firstname = Column(String(50), nullable=False)

        lastname = Column(String(50), nullable=False)

        username = Column(String(50), unique=True, nullable=False)

        email = Column(String(80), unique=True, nullable=False)

        password = Column(String(128), nullable=False)
        
        role = Column(Enum(RoleEnum), default=RoleEnum.USER, nullable=False)

        is_active = Column(Boolean, default=True)

       





