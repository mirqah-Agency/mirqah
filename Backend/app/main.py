from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import engine, Base
from app.models import project_request

# إنشاء جميع الجداول في قاعدة البيانات تلقائياً إذا لم تكن موجودة
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mirqah API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to Mirqah API"}