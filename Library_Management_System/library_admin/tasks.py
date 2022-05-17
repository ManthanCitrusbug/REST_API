from celery import shared_task
from .models import Issued_Book
from django.db.models import Q
from django.core.mail import send_mail
from Library_Management_System import settings
from dateutil import parser

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return 'Done'


# @shared_task(bind=True)
# def send_mail_task(self,email,date):
#     print(email)
#     date_time = parser.parse(date)
#     query = Issued_Book.objects.filter(email=email, return_date=date_time.date())
#     print(query)
#     if query:
#         for i in query:
#             send_mail(
#                 subject = 'Returned Book on date {}'.format(i.return_date),
#                 message = 'We recived the book you returned...' + 
#                 '\n\nReturned Book Name : {}'.format(i.book) +
#                 '\nIssued Date : {}'.format(i.issued_date) +
#                 '\nReturn Date : {}'.format(i.return_date) +
#                 '\nYour Total Charge : {}'.format(i.total_charge) + '₹'
#                 ,
#                 from_email = settings.EMAIL_HOST_USER,
#                 recipient_list = [i.email],
#                 fail_silently = True,
#             )
#     return 'Mail Send....'


@shared_task(bind=True)
def send_mail_task(self,id):
    query = Issued_Book.objects.get(id=id)
    print(query.email)
    if query:
        for i in query:
            send_mail(
                subject = 'Returned Book on date {}'.format(i.return_date),
                message = 'We recived the book you returned...' + 
                '\n\nReturned Book Name : {}'.format(i.book) +
                '\nIssued Date : {}'.format(i.issued_date) +
                '\nReturn Date : {}'.format(i.return_date) +
                '\nYour Total Charge : {}'.format(i.total_charge) + '₹'
                ,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [i.email],
                fail_silently = True,
            )
    return 'Mail Send....'