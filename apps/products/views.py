from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from elasticsearch_dsl import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from apps.products import serializers, models
from apps.products.documents import ProductDocument


class CategoryViewSet(ModelViewSet):
    """
    A viewset for viewing, editing and creating category instances.
    """
    queryset = models.Category.objects.all().order_by('title')
    serializer_class = serializers.CategorySerializer


class ProductViewSet(ModelViewSet):
    """
    A viewset for viewing, editing and creating product instances.
    """
    queryset = models.Product.objects.select_related('category').all().order_by('title')
    serializer_class = serializers.ProductSerializer
    document_class = ProductDocument

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('q', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('category_id', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
        ]
    )
    @action(methods=['get'], detail=False)
    def search(self, request, *args, **kwargs):
        search = self.document_class.search()

        search_query = request.query_params.get('q')
        category_id = request.query_params.get('category_id')

        if search_query:
            search = search.query(
                Q(
                    name_or_query="multi_match",
                    query=search_query,
                    fuzziness="auto",
                    fields=["title", "description"]
                )
            )
        if category_id:
            search = search.filter('term', category__id=category_id)

        search = search.sort(
            {"_score": {"order": "desc"}},
        )

        results = self.paginate_queryset(search)

        serializer = self.get_serializer(results, many=True)
        return self.get_paginated_response(serializer.data)
