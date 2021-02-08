from hammer.celery import app
from .service import email
from celery.contrib.abortable import AsyncResult


@app.task(bind=True, default_retry_delay=5 * 60)
def send_task_email(message, message2, message3):
    """Функия принимает текст, если все
    заполнено верно отправляет запускает функцию email
    в которой отправлет текст в указаное время"""
    email(message2, message3)
