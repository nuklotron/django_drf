# Generated by Django 4.2.4 on 2023-09-19 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0010_payments_payment_id_payments_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='payed_lesson',
        ),
    ]