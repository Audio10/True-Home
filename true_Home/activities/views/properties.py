# Django REST Framework
from rest_framework import viewsets
from activities.models.properties import Property
from activities.serializers.properties import PropertyModelSerializer
from rest_framework.exceptions import MethodNotAllowed

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter


class PropertyViewSet(viewsets.ModelViewSet):

    serializer_class = PropertyModelSerializer
    lookup_field = 'id'
    filter_backends = (SearchFilter, OrderingFilter)
    ordering = ('status', 'title')
    ordering_fields = ('status', 'title')
    search_fields = ('title',)

    def get_queryset(self):
        queryset = Property.objects.all()
        return queryset

    def perform_destroy(self, instance):
        instance.status = "Disabled"
        instance.save()

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')


