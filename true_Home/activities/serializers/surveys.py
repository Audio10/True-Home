from rest_framework import serializers
from activities.models.surveys import Survey


class SurveyModelSerializer(serializers.ModelSerializer):
    """Survey model serializer."""

    class Meta:
        model = Survey
        fields = (
            'id',
            'answers',
            'created_at',
            'activity'
        )

    def create(self, validated_data):
        property_id = self.context['activity_id']
        activity = Survey.objects.create(
            answers=validated_data['answers'],
            activity=property_id
        )
        return activity
