from fastapi import FastAPI
from app.api import books, auth
from app.db.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Review Service", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router)
app.include_router(auth.router, prefix="/auth", tags=["auth"])
@app.get("/")
def root():
    return {"message": "Welcome to Book Review Service"}
