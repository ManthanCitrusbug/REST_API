# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from django.conf import settings

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Library_Management_System.settings')
# app = Celery('Library_Management_System',include=['Library_Management_System.celery'],broker=settings.CELERY_BROKER_URL,backend=settings.CELERY_BROKER_URL)
# # app = Celery('Library_Management_System')

# app.conf.enable_utc = False

# app.conf.update(timezone = 'Asia/Kolkata')

# app.config_from_object(settings, namespace = 'CELERY')

# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     # print('Request: {0!r}'.format(self.request))
#     print(f'Request: {self.request!r}')


from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Library_Management_System.settings')
app = Celery('Library_Management_System')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))