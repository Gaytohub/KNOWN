
# cmd运行: celery -A config worker -l info (-A 默认寻找目录下的celery模块)
# 启动celery服务

from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings

# 设置环境变量
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
# 实例化Celery
app = Celery('config')
# 使用django的settings文件配置celery
app.config_from_object('django.conf:settings', 'CELERY')
# Celery加载所有注册应用中的tasks.py
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
