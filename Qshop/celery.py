import os
from celery import Celery
from django.conf import settings

# 设置celery的环境变量和django-celery的主目录
os.environ.setdefault('DJANGO_SETTINGS-MODULE','CeleryTask.settings')
# 实例化一个celery应用
app=Celery('art_project')


# 加载celery配置
app.config_from_object('django.conf:settings')

# 如果在项目当中，创建了task.py,celery就会沿着app去寻找这个文件
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)