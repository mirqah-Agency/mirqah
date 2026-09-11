from sqlalchemy import Column, Integer, String, Text
from app.database.connection import Base

class ProjectRequest(Base):
    __tablename__ = "project_requests"

    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    project_type = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)