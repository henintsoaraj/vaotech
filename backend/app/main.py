from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models.article import Base

app = FastAPI(title="vaotech API")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/articles")
def get_articles():
    # On branchera la BDD ici plus tard
    return {"articles": [], "total": 0}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/status")
def status():
    return {"nom": "vaotech", "version": "1.0.0", "statut": "running"}
