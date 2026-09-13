from sqlalchemy import Column, Integer, String, Text
from app.database.connection import Base

class ProjectRequest(Base):
    __tablename__ = "project_requests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    project_type = Column(String, nullable=False)
    details = Column(Text, nullable=True)
    
    # إذا كنت حاب تضيف project_budget اللي كنت تحاول تكتبه، ضفه هنا
    # لكن تذكر لازم تضيفه أيضاً في ملف schemas/project_request.py