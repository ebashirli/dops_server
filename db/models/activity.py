from sqlalchemy import Column, ForeignKey, Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from ..db_setup import Base

from datetime import datetime

class Activity(Base):
 __tablename__ = 'activities'

 id: Column(Integer, primary_key=True, index=True)
 activityId: str
 activityName: str
 moduleName: str
 coefficient: int
 currentPriority: float
 budgetedLaborUnits: float
 startDate: datetime
 finishDate: datetime
 cumulative: float
 isHidden: bool
