from sqlalchemy import Column, ForeignKey, Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from datetime import datetime
from ..db_setup import Base

class ReferenceDocument(Base):
 __tablename__ = 'referencedocuments'

 id: Column(Integer, primary_key=True, index=True)
 project: str
 referenceType: str
 moduleName: str
 documentNumber: str
 title: str
 transmittalNumber: str
 actionRequiredOrNext: bool
 receivedDate: datetime
 assignedTasksCount: int
 isHidden: bool
