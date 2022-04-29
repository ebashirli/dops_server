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

class ListName(Base):
 __tablename__ = 'listnames'
 
 id: Column(Integer, primary_key=True, index=True)
 name: str
 isHidden: bool

class ListItem(Base):
 __tablename__ = 'listitems'

 id: Column(Integer, primary_key=True, index=True)
 parentId: str
 item: str
 isHidden: bool

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

class Staff(Base):
 __tablename__ = 'staffs'

 id: Column(Integer, primary_key=True, index=True)
 badgeNo: str
 name: str
 surname: str
 patronymic: str
 fullName: str
 initial: str
 systemDesignation: str
 jobTitle: str
 email: str
 company: str
 dateOfBirth: datetime
 homeAddress: str
 startDate: datetime
 currentPlace: str
 contractFinishDate: datetime
 contact: str
 emergencyContact: str
 emergencyContactName: str
 note: str
 isHidden: bool

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

class Value(Base):
 __tablename__ = 'values'

 id: Column(Integer, primary_key=True, index=True)
 stageId: str
 employeeId: str
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