import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, serializers
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from lessons.models import Lesson, Course, Payments, CourseSubscriptions
from lessons.paginators import CoursePaginator
from lessons.permissions import IsModerator, IsOwner, IsSuper
from lessons.serializers import LessonSerializer, LessonListSerializer, CourseSerializer, \
    LessonDetailSerializer, PaymentsSerializer, CourseSubscriptionsSerializer, PaymentsCreateSerializer
from lessons.services import get_status_of_payment, get_stripe


class CourseViewSet(viewsets.ModelViewSet):
    """
    ViewSet for all actions with Course model (CRUD).
    Having permissions - IsAuthenticated, IsModerator, IsOwner, IsSuper.
    If you`re not in 'moderators' group, you would see in list only yours courses.
    After create/update course, 'owner' field would be filled automatically.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner | IsSuper]
    pagination_class = CoursePaginator

    def get_queryset(self):
        super_user = self.request.user.is_superuser
        moderators = self.request.user.groups.filter(name='moderators')
        owner = self.request.user

        if moderators or super_user:
            return self.queryset
        else:
            return Course.objects.filter(owner=owner.pk)

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
    """
    CreateAPIView for Lesson model.
    Having permissions - IsAuthenticated.
    """
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.owner = self.request.user
        new_obj.save()


class LessonListAPIView(generics.ListAPIView):
    """
    ListAPIView for Lesson model.
    Having permissions - IsAuthenticated.
    If you`re not in 'moderators' group or SU, you would see in list only yours lessons.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        super_user = self.request.user.is_superuser

        if super_user:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """
    RetrieveAPIView for Lesson model.
    Having permissions - IsAuthenticated.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """
    UpdateAPIView for Lesson model.
    Having permissions - IsAuthenticated, IsModerator, IsOwner, IsSuper.
    After updating lesson, 'owner' field would be filled automatically.
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner | IsSuper]

    def perform_update(self, serializer):
        updated_obj = serializer.save()
        if not self.request.user.is_staff:
            updated_obj.owner = self.request.user
        updated_obj.save()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """
    DestroyAPIView for Lesson model.
    Having permissions - IsAuthenticated, IsModerator, IsOwner, IsSuper.
    """
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner | IsSuper]


class PaymentsCreateAPIView(generics.CreateAPIView):
    """
    CreateAPIView for Payments model.
    Having permissions - IsAuthenticated.
    Working with 'services.py', initializing Stripe service, creating Payment URL
    and Payments Object
    """
    serializer_class = PaymentsCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        course = serializer.validated_data.get('payed_course')
        try:
            if self.request.user.is_authenticated:
                payment = serializer.save(user=self.request.user)
                payment.session = get_stripe(course, self.request.user)
                serializer.save(payment_id=payment.session.id, payment_status="created")
                payment.save()

        except serializers.ValidationError as er:
            print(f'There was an error in PaymentsCreateView - {er}')


class PaymentsListAPIView(generics.ListAPIView):
    """
    ListAPIView for Payments model.
    Having permissions - IsAuthenticated.
    """
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payed_course', 'method_of_payment',)
    ordering_fields = ('date_of_payment',)


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    """
    RetrieveAPIView for Payments model.
    Having permissions - IsAuthenticated.
    """
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payed_course', 'method_of_payment',)
    ordering_fields = ('date_of_payment',)


class PaymentsUpdateAPIView(generics.UpdateAPIView):
    """
    UpdateAPIView for Payments model.
    Having permissions - IsAuthenticated.
    """
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]


class PaymentsDestroyAPIView(generics.DestroyAPIView):
    """
    DestroyAPIView for Payments model.
    Having permissions - IsAuthenticated.
    """
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated]


class CourseSubscriptionsCreateAPIView(generics.CreateAPIView):
    """
    CreateAPIView for CourseSubscriptions model.
    Having permissions - IsAuthenticated.
    """
    serializer_class = CourseSubscriptionsSerializer
    queryset = CourseSubscriptions.objects.all()
    permission_classes = [IsAuthenticated]


class CourseSubscriptionsUpdateAPIView(generics.UpdateAPIView):
    """
    UpdateView for CourseSubscriptions model.
    Having permissions - IsAuthenticated.
    """
    serializer_class = CourseSubscriptionsSerializer
    queryset = CourseSubscriptions.objects.all()
    permission_classes = [IsAuthenticated]
