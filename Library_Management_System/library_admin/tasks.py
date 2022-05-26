from celery import shared_task
from .models import Issued_Book
from django.core.mail import send_mail
from Library_Management_System import settings
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
 
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
        # for i in query:
            send_mail(
                subject = 'Returned Book on date {}'.format(query.return_date),
                message = 'We recived the book you returned...' + 
                '\n\nReturned Book Name : {}'.format(query.book) +
                '\nIssued Date : {}'.format(query.issued_date) +
                '\nReturn Date : {}'.format(query.return_date) +
                '\nYour Total Charge : {}'.format(query.total_charge) + '₹'
                ,
                from_email = 'manthanmevada45115@gmail.com',
                recipient_list = ['manthan.citrusbug@gmail.com'],
                fail_silently = True,
            )
    return 'Mail Send....'


# @shared_task(bind=True)
# def send_mail_task(self,id):
#     query = Issued_Book.objects.get(id=id)
#     print(query.email)
#     message = Mail(
#         from_email = 'manthan.citrusbug@gmail.com',
#         to_emails = query.email,
#         subject = 'Returned Book on date {}'.format(query.return_date),            
#         plain_text_content = 'We recived the book you returned...' + 
#         '\n\nReturned Book Name : {}'.format(query.book) +
#         '\nIssued Date : {}'.format(query.issued_date) +
#         '\nReturn Date : {}'.format(query.return_date) +
#         '\nYour Total Charge : {}'.format(query.total_charge) + '₹'
#         ,
#     )
#     sg = SendGridAPIClient(settings.EMAIL_HOST_PASSWORD)            
#     # response = sg.send(message)
#     sg.send(message)
#     # try:
#     #     print(response.status_code)
#     #     print(response.body)
#     #     print(response.headers)
#     # except Exception as e:
#     #     print(e.message)
#     return 'Mail Send....'