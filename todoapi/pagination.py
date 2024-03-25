from rest_framework import pagination


class PagePagination(pagination.PageNumberPagination):
    max_page_size = 500
    page_size = 2
    page_query_param = 'pg'