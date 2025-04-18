from celery import Celery

celery_app = Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task(name='registrar_log')
def registrar_log(usuario, fecha):
    with open('logs_signin.txt', 'a+') as file:
        file.write(f'{usuario} - inicio de sesión: {fecha}\n')