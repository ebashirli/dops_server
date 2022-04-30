from turtle import clear
from sqlalchemy import Column, ForeignKey, Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from ..db_setup import Base
from datetime import datetime

class Value(Base):
 __tablename__ = 'values'

 id: Column(Integer, primary_key=True, index=True)
 stageId: str
 assignedBy: str
 assignedDateTime: datetime
 unassignedBy: int
 unassignedDateTime: datetime
 submitDateTime: datetime
 linkingToGroupDateTime: datetime
 phase: int
 weight: int
 gas: int
 sfd: int
 dtl: int
 hold: str
 note: str
 fileNames: list[str]
 isCommented: bool
 isHidden: bool
 user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

 assigned_user = relationship("User", back_populates="value")