from fastapi import FastAPI
from app.routers import project_requests  # استيراد ملف المسارات اللي سويناه
from app.database.connection import engine
from app.models import project_request as models

# هذا السطر بيمسح الجداول القديمة
models.Base.metadata.drop_all(bind=engine) 

# وهذا السطر بيبنيها من جديد بالتحديثات الأخيرة
models.Base.metadata.create_all(bind=engine)

# هذا السطر مهم: ينشئ الجداول في قاعدة البيانات بناءً على ملفات الـ Models
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mirqah API")

# هنا نربط مسار طلبات المشاريع بالسيرفر الأساسي
app.include_router(project_requests.router)

@app.get("/")
def root():
    return {"message": "مرحباً بك في الباك إند الخاص بمِرقاة!"}