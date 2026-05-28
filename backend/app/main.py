from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models.article import Base
from fastapi import Depends
from app.dependencies import get_db
from app.models.article import Article
from app.services.scraper import fetch_hackernews, save_articles

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
def get_articles(db = Depends(get_db)):
    
    # On branchera la BDD ici plus tard
    articles = db.query(Article).all()
    return {"articles": articles, "total": len(articles)}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/status")
def status():
    return {"nom": "vaotech", "version": "1.0.0", "statut": "running"}

@app.get("/scrape")
def scrape(db = Depends(get_db)):
    articles = fetch_hackernews()
    save_articles(db, articles)
    return {"saved": len(articles)}