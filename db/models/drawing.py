from sqlalchemy import Column, ForeignKey, Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from ..db_setup import Base

from datetime import datetime

class Drawing(Base):
 __tablename__ = 'drawings'

 id: Column(Integer, primary_key=True, index=True)
 activityCodeId: str
 drawingNumber: str
 drawingTitle: str
 module: str
 level: str
 area: list[str]
 drawingTag: list[str]
 functionalArea: str
 structureType: str
 note: str
 drawingCreateDate: datetime
 isHidden: bool

