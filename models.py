from datetime import datetime
from pydantic import BaseModel

class Activity(BaseModel):
 id: str | None = None
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

class Drawing(BaseModel):
 id: str | None = None
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

class Issue(BaseModel):
 id: str | None = None
 groupNumber: int 
 creationDate: datetime 
 createdBy: str 
 closeDate: datetime 
 linkedTaskIds: list[str]
 note: str 
 files: list[str]
 issueDate: datetime
 isHidden: bool

class ListName(BaseModel):
 id: str | None = None
 name: str
 isHidden: bool

class ListItem(BaseModel):
 id: str | None = None
 parentId: str
 item: str
 isHidden: bool

class ReferenceDocument(BaseModel):
 id: str | None = None
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

class Staff(BaseModel):
 id: str | None = None
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

class Stage(BaseModel):
 id: str | None = None
 taskId: str
 index: int
 checkerCommentCounter: int
 reviewerCommentCounter: int
 creationDateTime: datetime
 note: str
 isHidden: bool

class TaskModel(BaseModel):
 id: str | None = None
 parentId: str
 revisionMark: str
 referenceDocuments: list[str]
 changeNumber: int
 holdReason: str
 note: str
 creationDate: datetime
 isHidden: bool

class ValueModel(BaseModel):
 id: str | None = None
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