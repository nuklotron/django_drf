# Generated by Django 4.2.4 on 2023-09-16 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0005_remove_course_user_course_remove_lesson_users_lesson_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSubscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='status')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.course', verbose_name='course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'subscription status',
                'verbose_name_plural': 'subscriptions status',
            },
        ),
    ]
