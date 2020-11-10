# Django REST Framework
from rest_framework import status, viewsets
from activities.models.surveys import Survey
from activities.models.activities import Activity
from activities.serializers.surveys import SurveyModelSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


class SurveyViewSet(viewsets.ModelViewSet):

    serializer_class = SurveyModelSerializer
    lookup_field = 'id'

    def dispatch(self, request, *args, **kwargs):
        """Verify that the circle exists."""
        activity_id = kwargs['activity_id']
        self.activity = get_object_or_404(Activity, id=activity_id)
        return super(SurveyViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Survey.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = SurveyModelSerializer(
            data=request.data,
            context={'activity_id': self.activity}
        )

        serializer.is_valid(raise_exception=True)
        activity = serializer.save()
        data = self.get_serializer(activity).data
        return Response(data, status=status.HTTP_201_CREATED)
