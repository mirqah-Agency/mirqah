from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import project_requests  # استيراد ملف المسارات اللي سويناه
from app.database.connection import engine
from app.models import project_request as models

# ينشئ الجداول فقط إذا ما كانت موجودة (وحذفنا سطر المسح عشان نحمي بياناتك)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mirqah API")

# إعدادات الـ CORS لتصريح الفرونت إند
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # النجمة تعني السماح لجميع الروابط مؤقتاً أثناء التطوير
    allow_credentials=True,
    allow_methods=["*"], # السماح بجميع العمليات مثل POST و GET
    allow_headers=["*"],
)

# هنا نربط مسار طلبات المشاريع بالسيرفر الأساسي
app.include_router(project_requests.router)

@app.get("/")
def root():
    return {"message": "مرحباً بك في الباك إند الخاص بمِرقاة!"}