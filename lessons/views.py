from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from lessons.models import Lesson, Course, Payments, CourseSubscriptions
from lessons.paginators import CoursePaginator
from lessons.permissions import IsModerator, IsOwner, IsSuper
from lessons.serializers import LessonSerializer, LessonListSerializer, CourseSerializer, \
    LessonDetailSerializer, PaymentsSerializer, CourseSubscriptionsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner | IsSuper]
    pagination_class = CoursePaginator

    def get_queryset(self):
        if not self.request.user.groups.filter(name='moderators'):
            return Course.objects.filter(owner=self.request.user)
        return Course.objects.all()

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.owner = self.request.user
        new_obj.save()

    def perform_update(self, serializer):
        updated_obj = serializer.save()
        if not self.request.user.is_staff:
            updated_obj.owner = self.request.user
        updated_obj.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.owner = self.request.user
        new_obj.save()


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.groups.filter(name='moderators'):
            return Lesson.objects.filter(owner=self.request.user)
        return Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner | IsSuper]

    def perform_update(self, serializer):
        updated_obj = serializer.save()
        if not self.request.user.is_staff:
            updated_obj.owner = self.request.user
        updated_obj.save()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner | IsSuper]


class PaymentsCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payed_lesson', 'payed_course', 'method_of_payment',)
    ordering_fields = ('date_of_payment',)


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payed_lesson', 'payed_course', 'method_of_payment',)
    ordering_fields = ('date_of_payment',)


class PaymentsUpdateAPIView(generics.UpdateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]


class PaymentsDestroyAPIView(generics.DestroyAPIView):
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]


class CourseSubscriptionsCreateAPIView(generics.CreateAPIView):
    serializer_class = CourseSubscriptionsSerializer
    queryset = CourseSubscriptions.objects.all()
    permission_classes = [IsAuthenticated]


class CourseSubscriptionsUpdateView(generics.UpdateAPIView):
    serializer_class = CourseSubscriptionsSerializer
    queryset = CourseSubscriptions.objects.all()
    permission_classes = [IsAuthenticated]
