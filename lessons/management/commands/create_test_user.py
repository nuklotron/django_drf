from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='test@test.com',
            first_name='Test',
            last_name='Testov',
            is_staff=False,
            is_superuser=False
        )

        user.set_password('Test')
        user.save()
