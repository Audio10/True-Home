from activities.models.properties import Property
from rest_framework import serializers


class PropertyModelSerializer(serializers.ModelSerializer):
    """Property model serializer."""

    class Meta:

        model = Property
        fields = (
            'id',
            'title',
            'address'
        )

        read_only_fields = (
            'created_at',
            'updated_at',
            'disabled_at',
        )

    def create(self, validated_data):
        return Property.objects.create(**validated_data, status="Active")

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.address = validated_data['address']
        instance.status = "Active"
        instance.save()
        return instance

