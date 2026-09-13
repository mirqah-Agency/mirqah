from pydantic import BaseModel
from typing import Optional

# 1. القالب الأساسي: يحتوي على البيانات المشتركة
class ProjectRequestBase(BaseModel):
    name: str
    phone: str
    email: str
    project_type: str
    details: Optional[str] = None

# 2. قالب الإنشاء: وقت استقبال طلب جديد
class ProjectRequestCreate(ProjectRequestBase):
    pass

# 3. قالب الرد: هذا هو الكلاس اللي ضاع وكان السيرفر يبحث عنه!
class ProjectRequestResponse(ProjectRequestBase):
    id: int

    class Config:
        from_attributes = True