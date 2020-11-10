from rest_framework import mixins, status, viewsets
from rest_framework.generics import get_object_or_404
# Models
from activities.models.activities import Activity
from activities.models.properties import Property

from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed

# Serializers
from activities.serializers.activities import ActivitySerializer, ActivityUpdateSerializer

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter


class ActivityViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):

    serializer_class = ActivitySerializer
    lookup_field = 'id'
    filter_backends = (SearchFilter, OrderingFilter)
    ordering = ('status', 'schedule')
    ordering_fields = ('status', 'schedule')
    search_fields = ('title',)

    def dispatch(self, request, *args, **kwargs):
        """Verify that the circle exists."""
        property_id = kwargs['property_id']
        self.property = get_object_or_404(Property, id=property_id)
        return super(ActivityViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """Return circle members."""
        return Activity.objects.filter(
            property=self.property
        )

    def create(self, request, *args, **kwargs):
        serializer = ActivitySerializer(
            data=request.data,
            context={'property_id': self.property}
        )

        serializer.is_valid(raise_exception=True)
        activity = serializer.save()
        data = self.get_serializer(activity).data
        return Response(data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        serializer = ActivityUpdateSerializer(
            data=request.data,
            context={'activity_id': kwargs['id']}
        )
        serializer.is_valid(raise_exception=True)
        activity = serializer.save()
        data = self.get_serializer(activity).data
        return Response(data, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.status = "Cancel"
        instance.save()

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')
