from sqlalchemy import (
 Column,
 ForeignKey,
 Boolean,
 Column,
 ForeignKey,
 Integer,
 String,
 Enum,
 Text
)
from sqlalchemy.orm import relationship

from datetime import datetime
from ..db_setup import Base

class Staff(Base):
 __tablename__ = 'staffs'

 id: Column(Integer, primary_key=True, index=True)
 badgeNo: Column(String(50), )
 name: Column(String(50), )
 surname: Column(String(50), )
 patronymic: Column(String(50), )
 fullName: Column(String(50), )
 initial: Column(String(50), )
 systemDesignation: Column(String(50), )
 jobTitle: Column(String(50), )
 email: Column(String(50), )
 company: Column(String(50), )
 dateOfBirth: Column(datetime, ) 
 homeAddress: Column(String(50), )
 startDate: Column(datetime, )
 currentPlace: Column(String(50), )
 contractFinishDate: Column(datetime, )
 contact: Column(String(50), )
 emergencyContact: Column(String(50), )
 emergencyContactName: Column(String(50), )
 note: Column(String(50), )
 isHidden: Column(bool, )
