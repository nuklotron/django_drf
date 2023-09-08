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

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons_in_course',)

    def get_lessons_in_course(self, instance):
        return instance.lesson_set.all().count()


class CourseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        lesson_data = validated_data.pop('lessons')
        courses = Course.objects.create(**validated_data)
        for data in lesson_data:
            lesson_object, flag = Lesson.objects.get_or_create(title=data['title'],
                                                               defaults={
                                                                   'description': data['description'],
                                                                   'video_url': data['video_url']
                                                               })
            courses.lessons.add(lesson_object)
        return courses


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_in_course = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, required=False)

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



