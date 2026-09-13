from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db  # ملف الاتصال بقاعدة البيانات اللي سويناه سابقاً
from app.schemas import project_request as schemas
from app.crud import project_request as crud

# إنشاء مسار جديد مخصص لطلبات المشاريع
router = APIRouter(
    prefix="/requests",
    tags=["Project Requests"]
)

# مسار إنشاء طلب جديد (POST)
@router.post("/", response_model=schemas.ProjectRequestResponse)
def create_request_endpoint(request: schemas.ProjectRequestCreate, db: Session = Depends(get_db)):
    # الدالة تستقبل الطلب، وتمرره للـ CRUD ليتم حفظه
    return crud.create_request(db=db, request=request)