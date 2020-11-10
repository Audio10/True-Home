from django.utils import timezone
from rest_framework import serializers
from activities.models.activities import Activity
from activities.serializers.properties import PropertyModelSerializer


class ActivitySerializer(serializers.ModelSerializer):
    """Activity model serializer."""

    property_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    condition = serializers.SerializerMethodField()

    property = PropertyModelSerializer(read_only=True)
    survey = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Activity
        fields = (
            'id',
            'title',
            'schedule',
            'property_id',
            'created_at',
            'condition',
            'status',
            'property',
            'survey',
        )

        read_only_fields = (
            'status',
        )

    def get_condition(self, instance):

        if "Active" in instance.status:
            if instance.schedule < timezone.now():
                return "Atrasada"
            else:
                return "Pendiente a realizar "
        elif "Done" in instance.status:
            return "Finalizada"
        else:
            return "Cancelada"

    def validate(self, data):
        q = Activity.objects.filter(schedule=data['schedule'])

        property_status = self.context['property_id'].status
        if "Disabled" in property_status:
            raise serializers.ValidationError('You can create a new activity for a disabled property.')

        q = Activity.objects.filter(schedule=data['schedule'])
        if q.exists():
            raise serializers.ValidationError("There is already an activity registered for this day.")

        return data

    def create(self, validated_data):
        property_id = self.context['property_id'].id
        activity = Activity.objects.create(
            title=validated_data['title'],
            schedule=validated_data['schedule'],
            property_id=property_id,
            status="Active"
        )

        return activity


class ActivityUpdateSerializer(serializers.Serializer):

    schedule = serializers.DateTimeField()

    def validate(self, data):
        activity_id = self.context['activity_id']
        activity = Activity.objects.get(id=activity_id)
        if "Cancel" in activity.status:
            raise serializers.ValidationError('You cannot reschedule a canceled activity.')

        return data

    def create(self, validated_data):
        activity_id = self.context['activity_id']
        activity = Activity.objects.get(id=activity_id)
        activity.schedule = validated_data['schedule']
        activity.save()
        return activity

    def update(self, instance, validated_data):
        pass
