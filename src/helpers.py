import smtplib

from celery import shared_task

from core import settings


@shared_task
def send_mail_to_user(user: str, title: str, executed: int) -> None:
    port = settings.EMAIL_PORT
    smtp_server = settings.EMAIL_HOST
    sender_email = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(sender_email, password)
        server.send_mail(
            'Task was moved',
            f'{title} was moved to {executed}',
            'todo@example.com',
            [f'{user}'],
            fail_silently=False,
        )
