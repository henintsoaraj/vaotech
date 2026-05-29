from app.workers.celery_app import celery_app
from app.services.scraper import fetch_hackernews, save_articles
from app.database import SessionLocal

@celery_app.task
def scrape_task():
    db = SessionLocal()
    try:
        articles = fetch_hackernews()
        save_articles(db, articles)
    finally:
        db.close()
        