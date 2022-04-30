from sqlalchemy import Column, ForeignKey, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..db_setup import Base

class ListName(Base):
 __tablename__ = 'listnames'
 
 id: Column(Integer, primary_key=True, index=True)
 name: Column(String(50), nullable=False)
 isHidden: Column(Boolean, default=False)
 
 item = relationship("ListItem", back_populates="header", uselist=False)

class ListItem(Base):
 __tablename__ = 'listitems'

 id: Column(Integer, primary_key=True, index=True)
 item_name: Column(String(50), nullable=False)
 isHidden: Column(Boolean, default=False)
 name_id = Column(Integer, ForeignKey("listnames.id"), nullable=False)

 header = relationship("ListName", back_populates="item")

