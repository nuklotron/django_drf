from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from lessons.models import Lesson, Course, Payments


class LessonSerializer(serializers.ModelSerializer):
    courses = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_in_course = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_in_course(self, instance):
        return instance.lesson_set.all().count()


class LessonDetailSerializer(serializers.ModelSerializer):
    courses = CourseSerializer()

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):
    courses = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'description', 'courses',)


class PaymentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'
