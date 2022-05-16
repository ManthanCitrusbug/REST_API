from email import message
from celery import shared_task
from .models import Issued_Book
from django.db.models import Q
from django.core.mail import send_mail
from Library_Management_System import settings

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return 'Done'


@shared_task(bind=True)
def send_mail_task(self):
    # query = Issued_Book.objects.filter(total_charge__isnull=True)
    query = Issued_Book.objects.filter()
    if query:
        for i in query:
            send_mail(
                subject = 'Returned Book on date' + i.return_date,
                message = 'We recived the book you returned...' + 
                'Returned Book Name :' + i.book +
                'Issued Date :' + i.issued_book +
                'Return Date :' + i.return_date +
                'Your Total Charge :' + i.total_charge + '₹'
                ,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [i.email],
                fail_silently = True,
            )
    return 'Mail Send....'