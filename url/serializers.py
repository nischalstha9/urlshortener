from rest_framework import serializers
from .models import urls
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

class UrlListSerializer(ModelSerializer):
    class Meta:
        model = urls
        fields = ['nlong','short']


class PostSearchAPIView(ListAPIView):
    serializer_class = UrlListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nlong']
    def get_queryset(self, *args, **kwargs):
        queryset_list = urls.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(nlong__icontains=query)
            ).distinct()
        return queryset_list