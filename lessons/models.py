from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='course')
    preview_img = models.ImageField(upload_to='course/', verbose_name='preview', **NULLABLE)
    description = models.TextField(verbose_name='description')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='course_owner', **NULLABLE)
    price = models.IntegerField(default=0, verbose_name='price')

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
    CARD = 'card'

    PAYMENTS_TYPE = (
        (CASH, 'Cash'),
        (CARD, 'Card')
    )

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='user')
    date_of_payment = models.DateField(auto_now_add=True, verbose_name='date_of_payment')
    payed_course = models.ForeignKey('Course', on_delete=models.SET_NULL, verbose_name='payed_course', **NULLABLE)
    summ = models.IntegerField(verbose_name='summ')
    method_of_payment = models.CharField(max_length=15, choices=PAYMENTS_TYPE, verbose_name='method_of_payment')
    payment_status = models.CharField(max_length=100, verbose_name='payment_status', **NULLABLE)
    payment_id = models.CharField(max_length=100, verbose_name='payment_id', **NULLABLE)

    def __str__(self):
        return f'{self.payment_id}'

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
        ordering = ('user',)


class CourseSubscriptions(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='course')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='user')
    status = models.BooleanField(verbose_name='status')

    def __str__(self):
        if self.status:
            return f'{self.user} is subscribed to {self.course}'
        else:
            return f'{self.user} is`nt subscribed to {self.course}'

    class Meta:
        verbose_name = 'subscription status'
        verbose_name_plural = 'subscriptions status'
