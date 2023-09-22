from datetime import datetime, timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from lessons.models import Payments
from lessons.services import get_status_of_payment
from users.models import User


@shared_task
def payments_status_update():
    """
    This method checking status of Payment.
    If payment complete status would be changed in DB.
    """
    payments = Payments.objects.filter(payment_status='created')
    for payment in payments:
        if payment:
            check_status = get_status_of_payment(payment.payment_id)
            status = check_status.get('status')
            if status != 'open':
                payment.payment_status = status
                print(f'Status was changed to {status}')
                payment.save()


@shared_task
def user_last_login_check():
    """
    If user was inactive more than 28 days his account would be deactivated
    """
    date_now = datetime.now()
    date_delta = date_now - timedelta(days=28)
    user = User.objects.filter(last_login__lte=date_delta, is_active=True)
    user.update(is_active=False)


@shared_task
def send_subscription(user_id):
    """
    Email notification when new subscription created
    """
    user = User.objects.get(pk=user_id)
    send_mail(
        subject='New subscription',
        message=f'You are subscribed for new course!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )
