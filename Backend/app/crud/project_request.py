from sqlalchemy.orm import Session
from app.models import project_request as models
from app.schemas import project_request as schemas

def create_request(db: Session, request: schemas.ProjectRequestCreate):
    # تحويل البيانات الجاية من الواجهة إلى كائن يقبله الداتا بيس
    db_request = models.ProjectRequest(**request.model_dump())
    
    # إضافة الطلب للجدول وحفظه
    db.add(db_request)
    db.commit()
    db.refresh(db_request) # تحديث البيانات عشان ناخذ الـ ID الجديد
    
    return db_request