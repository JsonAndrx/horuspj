import os
from datetime import timedelta
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')


BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
CELERY_BROKER_URL = os.environ.get('REDIS_URL')
app.conf.broker_url = BASE_REDIS_URL


app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'America/Bogota'

app.conf.beat_schedule = {
    'eliminando-registros':{
        'task':'horus.tasks.delete_register',
        'schedule':timedelta(seconds=30),
    },'eliminando-registros-expirados':{
        'task':'horus.tasks.delete_register_expired',
        'schedule':timedelta(seconds=30),
    }
}

app.autodiscover_tasks()