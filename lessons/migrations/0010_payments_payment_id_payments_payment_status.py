# Generated by Django 4.2.4 on 2023-09-18 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0009_alter_payments_method_of_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='stipe_payment_id'),
        ),
        migrations.AddField(
            model_name='payments',
            name='payment_status',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='payment_status'),
        ),
    ]
