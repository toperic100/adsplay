from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Ad(Base):
    __tablename__ = "ads"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    video_url = Column(String)
