from rest_framework import viewsets, filters
from apps.news.models import News
from apps.api.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['published_at']
    ordering_fields = ['published_at']
