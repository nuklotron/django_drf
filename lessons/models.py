from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='course')
    preview_img = models.ImageField(upload_to='course/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f'Course: {self.title}'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='lesson')
    preview_img = models.ImageField(upload_to='lessons/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    video_url = models.URLField(verbose_name='video url', **NULLABLE)

    def __str__(self):
        return f'Lesson: {self.title}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
