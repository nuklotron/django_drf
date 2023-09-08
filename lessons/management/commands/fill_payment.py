from django.core.management import BaseCommand
from lessons.models import Payments
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user_payment = Payments.objects.create(
            user=2,
            summ=1000,
            payed_course=[37],
            method_of_payment="cash"
        )
        user_payment.save()
