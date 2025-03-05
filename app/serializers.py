from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'organizer']

    def create(self, validated_data):
        user = self.context['request'].user
        event = Event.objects.create(organizer=user, **validated_data)
        return event
