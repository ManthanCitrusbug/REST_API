from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class Mypagination(PageNumberPagination):
    page_size = 5
    max_page_size = 10