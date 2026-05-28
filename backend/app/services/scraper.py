import httpx
from app.models.article import Article

BASE_URL = "https://hacker-news.firebaseio.com/v0"

def fetch_hackernews():
    r = httpx.get(f"{BASE_URL}/topstories.json")
    top_ids = r.json()[:30]
    
    articles = []
    for id in top_ids:
        detail = httpx.get(f"{BASE_URL}/item/{id}.json")
        d = detail.json()
        articles.append({
            "title":  d.get("title", "Sans titre"),
            "url":    d.get("url", f"https://news.ycombinator.com/item?id={id}"),
            "source": "hackernews",
            "score":  d.get("score", 0),
        })
    
    return articles

def save_articles(db, articles):
    for a in articles:
        article = Article(
            title = a["title"],
            url = a["url"],
            source = a["source"],
            score = a["score"],
        )
        db.add(article)
    db.commit()