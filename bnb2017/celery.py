from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery import shared_task

#from stockmarket.tasks import *

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bnb2017.settings')

app = Celery('bnb2017')
# app.conf.BROKER_URL = 'amqp://{}:{}@{}'.format(settings.AMQP_USER, settings.AMQP_PASSWORD, settings.AMQP_HOST)
# app.conf.CELERY_DEFAULT_EXCHANGE = 'myapp.celery'
# app.conf.CELERY_DEFAULT_QUEUE = 'myapp.celery_default'
# app.conf.CELERY_TASK_SERIALIZER = 'json'
# app.conf.CELERY_ACCEPT_CONTENT = ['json']
# app.conf.CELERY_IGNORE_RESULT = True
# app.conf.CELERY_DISABLE_RATE_LIMITS = True
# app.conf.BROKER_POOL_LIMIT = 2

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

# This works
# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'tasks.revise_stock_price_by_news',
#         'schedule': 5.0,
#         #'args': (16, 16)
#     },
# }

app.conf.update(CELERY_TIMEZONE = 'Asia/Kolkata')

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

