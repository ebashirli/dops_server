from sqlalchemy import Column, ForeignKey, Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from ..db_setup import Base

from datetime import datetime

class Task(Base):
 __tablename__ = 'tasks'

 id: Column(Integer, primary_key=True, index=True)
 parentId: str
 revisionMark: str
 referenceDocuments: list[str]
 changeNumber: int
 holdReason: str
 note: str
 creationDate: datetime
 isHidden: bool