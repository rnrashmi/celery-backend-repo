import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

app = Celery("dcelery")

app.conf.from_object("django.conf.settings", namespce="CELERY")

@app.task
def add_number():
    return

app.autodiscover_tasks()