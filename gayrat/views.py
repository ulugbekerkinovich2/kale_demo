import django_filters
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from gayrat.models import Product
from gayrat.serializers import Product1Serializer


class ProductStandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    max_page_size = 100


class ProductViewSets(mixins.ListModelMixin, GenericViewSet):
    queryset = Product.objects.prefetch_related("shots").select_related("category")
    serializer_class = Product1Serializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["best_seller_product", "saralangan", "category_id"]
    pagination_class = ProductStandardResultsSetPagination
