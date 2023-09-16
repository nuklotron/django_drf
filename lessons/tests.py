from rest_framework import status
from rest_framework.test import APITestCase

from lessons.models import Course
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.com',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        self.user.set_password('password')
        self.user.save()
        response = self.client.post(
            '/users/token/',
            {'email': 'test@test.com', 'password': 'password'}
        )

        self.token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_course(self):
        """ testing course creation"""
        data = {
            'title': 'Test',
            'description': 'Test description',
            'owner': 'test@test.com'
        }

        response = self.client.post(
            "/courses/",
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'lessons_in_course': 0, 'lessons': [], 'owner': 'test@test.com', 'title': 'Test', 'preview_img': None, 'description': 'Test description'}
        )

    def test_list_course(self):
        """testing list of courses"""
        Course.objects.create(
            title='list test',
            description='list test'
        )
        response = self.client.get(
            '/courses/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 0, 'next': None, 'previous': None, 'results': []}
        )

