from django.contrib import admin

# Register your models here.
from lessons.models import Course, Lesson, Payments


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

    list_display = ('user', 'method_of_payment',)
    list_filter = ('user', 'method_of_payment',)
    search_fields = ('user', 'method_of_payment',)
