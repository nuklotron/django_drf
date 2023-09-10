from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from lessons.models import Lesson, Course, Payments
from lessons.serializers import LessonSerializer, LessonListSerializer, CourseSerializer, \
    LessonDetailSerializer, PaymentsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # def get_serializer_class(self):
    #     return self.serializers.get(self.action, self.default_serializer_class)

    # def get_queryset(self):
    #     if self.request.user.has_perms(['course.view_course']):
    #         return Course.objects.all()
    #     return Course.objects.filter(user_course=self.request.user)

    def perform_create(self, serializer):
        new_obj = serializer.save()
        # new_obj.user_course = self.request.user
        new_obj.save()

    def perform_update(self, serializer):
        updated_obj = serializer.save()
        # if not self.request.user.is_staff:
        #     updated_obj.user_course = self.request.user
        updated_obj.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
