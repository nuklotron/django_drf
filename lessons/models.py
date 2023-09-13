from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='course')
    preview_img = models.ImageField(upload_to='course/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='course_owner', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        ordering = ('id',)


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='lesson')
    preview_img = models.ImageField(upload_to='lessons/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    video_url = models.URLField(verbose_name='video url', **NULLABLE)
    courses = models.ForeignKey('Course', on_delete=models.SET_NULL, verbose_name='course', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='lesson_owner', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
        ordering = ('id',)


class Payments(models.Model):
    CASH = 'cash'
    REMITTANCE = 'remittance'

    PAYMENTS_TYPE = (
        (CASH, 'Cash'),
        (REMITTANCE, 'Remittance')
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='user')
    date_of_payment = models.DateField(auto_now_add=True, verbose_name='date_of_payment')
    payed_lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, verbose_name='payed_lesson', **NULLABLE)
    payed_course = models.ForeignKey('Course', on_delete=models.SET_NULL, verbose_name='payed_course', **NULLABLE)
    summ = models.IntegerField(verbose_name='summ')
    method_of_payment = models.CharField(max_length=15, choices=PAYMENTS_TYPE, verbose_name='method_of_payment')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
        ordering = ('user',)
