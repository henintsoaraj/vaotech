from app.services.scraper import fetch_hackernews

def test_fetch_hackernews():
    articles = fetch_hackernews()
    assert len(articles) > 0

def test_article_has_title():
    articles = fetch_hackernews()
    assert "title" in articles[0]

def test_article_has_url():
    articles = fetch_hackernews()
    assert "url" in articles[0]

