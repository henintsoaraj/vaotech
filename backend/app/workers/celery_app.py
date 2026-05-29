from celery import Celery

celery_app = Celery(
    "vaotech",
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

celery_app.autodiscover_tasks(["app.workers"])
celery_app.conf.beat_schedule = {
    "scrape-every-15-minutes": {
        "task": "app.workers.tasks",
        "schedule": 60*15,
    }
}