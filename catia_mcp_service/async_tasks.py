# 异步任务队列（Celery简单示例）
from celery import Celery
import os

celery_app = Celery('catia_tasks', broker=os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0'))


@celery_app.task
def long_running_task(args):
    # 这里可调用CATIA建模等耗时操作
    import time

    time.sleep(10)
    return {'status': 'done', 'result': 'ok'}
