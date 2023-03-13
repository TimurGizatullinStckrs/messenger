from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.message import MessageSerializer
from core.models import Message


class MessageViewSet(viewsets.GenericViewSet):
    permission_classes = IsAuthenticated

    def list(self, request):
        queryset = Message.objects.all()
        paginated_queryset = super().paginate_queryset(queryset)
        serialized = MessageSerializer(paginated_queryset, many=True)

        return Response(serialized, status=status.HTTP_200_OK)
