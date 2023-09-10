from django.urls import path

from lessons.apps import LessonsConfig
from lessons.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentsCreateAPIView, PaymentsListAPIView, PaymentsRetrieveAPIView, \
    PaymentsUpdateAPIView, PaymentsDestroyAPIView
from rest_framework.routers import DefaultRouter

app_name = LessonsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments_create'),
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path('payments/<int:pk>/', PaymentsRetrieveAPIView.as_view(), name='payments_detail'),
    path('payments/update/<int:pk>/', PaymentsUpdateAPIView.as_view(), name='payments_update'),
    path('payments/delete/<int:pk>/', PaymentsDestroyAPIView.as_view(), name='payments_delete'),
] + router.urls

