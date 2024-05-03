from celery import Celery

app = Celery('scheduler_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()