# Generated by Django 4.2.4 on 2023-09-12 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0003_remove_course_lessons_remove_payments_payed_course_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payments',
            options={'ordering': ('user',), 'verbose_name': 'payment', 'verbose_name_plural': 'payments'},
        ),
        migrations.AddField(
            model_name='lesson',
            name='users_lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_created'),
        ),
    ]
