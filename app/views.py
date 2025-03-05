from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .filters import EventFilter
from .models import Event
from .serializers import EventSerializer

@extend_schema_view(
    list=extend_schema(description="Get a list of all events."),
    create=extend_schema(description="Create a new event."),
    retrieve=extend_schema(description="Get details of a specific event."),
    update=extend_schema(description="Update an event."),
    destroy=extend_schema(description="Delete an event."),
    )


class EventViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = EventFilter
    search_fields = ['title', 'location', 'date']
