from sqlalchemy import Column, Integer, String
from app.database import Base

class Name(Base):
    __tablename__ = "names"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
