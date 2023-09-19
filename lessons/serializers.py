from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from lessons.models import Lesson, Course, Payments, CourseSubscriptions
from lessons.services import get_stripe
from lessons.validators import UrlValidator
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    courses = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    owner = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    validators = [UrlValidator(field='video_url')]

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_in_course = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    owner = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_in_course(self, instance):
        return instance.lesson_set.all().count()


class LessonDetailSerializer(serializers.ModelSerializer):
    courses = CourseSerializer()
    owner = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):
    courses = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'courses',)


class PaymentsSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    payed_course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Payments
        fields = '__all__'


class PaymentsCreateSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    payed_course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    payment_url = serializers.SerializerMethodField()

    class Meta:
        model = Payments
        fields = '__all__'

    def get_payment_url(self, instance):
        return get_stripe(instance.payed_course, instance.user).url


class CourseSubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscriptions
        fields = "__all__"
