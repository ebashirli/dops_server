from sqlalchemy import Column, ForeignKey, Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from ..db_setup import Base
from datetime import datetime

class Issue(Base):
 __tablename__ = 'issues'

 id: Column(Integer, primary_key=True, index=True)
 groupNumber: int 
 creationDate: datetime 
 createdBy: str 
 closeDate: datetime 
 linkedTaskIds: list[str]
 note: str 
 files: list[str]
 issueDate: datetime
 isHidden: bool

