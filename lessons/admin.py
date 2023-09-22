from django.contrib import admin

# Register your models here.
from lessons.models import Course, Lesson, Payments, CourseSubscriptions


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ('title',)
    list_filter = ('title', 'owner',)
    search_fields = ('title', 'owner',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    list_display = ('title', 'courses',)
    list_filter = ('title', 'courses',)
    search_fields = ('title', 'courses',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):

    list_display = ('user', 'date_of_payment', 'payment_status',)
    list_filter = ('user', 'payment_status',)
    search_fields = ('user', 'payment_status',)


@admin.register(CourseSubscriptions)
class CourseSubscriptionsAdmin(admin.ModelAdmin):

    list_display = ('course', 'user', 'status',)
    list_filter = ('course', 'user', 'status',)
    search_fields = ('course', 'user', 'status',)
