from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.base import Base

class ApiKey(Base):
    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    key = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=func.now())
