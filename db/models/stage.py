from sqlalchemy import Column, ForeignKey, Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from datetime import datetime
from ..db_setup import Base

class Stage(Base):
 __tablename__ = 'stages'

 id: Column(Integer, primary_key=True, index=True)
 taskId: str
 index: int
 checkerCommentCounter: int
 reviewerCommentCounter: int
 creationDateTime: datetime
 note: str
 isHidden: bool
