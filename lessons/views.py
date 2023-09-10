from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
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


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payed_lesson', 'payed_course', 'method_of_payment',)
    ordering_fields = ('date_of_payment',)


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payed_lesson', 'payed_course', 'method_of_payment',)
    ordering_fields = ('date_of_payment',)


class PaymentsUpdateAPIView(generics.UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer


class PaymentsDestroyAPIView(generics.DestroyAPIView):
    queryset = Payments.objects.all()
