from rest_framework.pagination import PageNumberPagination


class CoursePaginator(PageNumberPagination):
    page_size = 10


class LessonPaginator(PageNumberPagination):
    page_size = 10


class PaymentsPaginator(PageNumberPagination):
    page_size = 10


class CourseSubscriptionsPaginator(PageNumberPagination):
    page_size = 10
