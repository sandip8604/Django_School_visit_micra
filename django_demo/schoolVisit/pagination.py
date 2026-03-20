from rest_framework.pagination import PageNumberPagination

class SchoolPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'   # client can control size
    max_page_size = 50