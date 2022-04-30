import enum
from sqlalchemy import Column, ForeignKey, Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from ..db_setup import Base

class Role(enum.Enum):
 admin = 0
 coordinator = 1
 user = 2

class User(Base):
 __tablename__ = 'users'
 id = Column(Integer, primary_key=True, index=True)
 email = Column(String(100), unique=True, index=True, nullable=False)
 role = Column(Enum(Role))

 profile = relationship("Profile", back_populates="owner", uselist=False)
 value = relationship("Value", back_populates="assigned_user", uselist=True)

 

class Profile(Base):
 __tablename__ = 'profiles'

 id = Column(Integer, primary_key=True, index=True)
 first_name = Column(String(50), nullable=False)
 last_name = Column(String(50), nullable=False)
 patronymic = Column(String(50), nullable=True)
 note = Column(Text, nullable=True)
 is_active = Column(Boolean, default=False)
 user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

 owner = relationship("User", back_populates="profile")

