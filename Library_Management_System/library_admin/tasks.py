from celery import shared_task

@shared_task(bind=True)
def send_mail(self):
    for i in range(10):
        print(i)
    return 'Done'