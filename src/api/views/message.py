from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.message import MessageSerializer
from core.models import Message


class MessageViewSet(viewsets.GenericViewSet):
    permission_classes = IsAuthenticated

    def list(self, request):
        limit = request.data.get('limit', None)
        offset = request.data.get('offset', None)

        if limit is None or offset is None:
            return Response({'Message': 'Missing required params (limit, offset)'}, status=status.HTTP_400_BAD_REQUEST)

        queryset = Message.objects.all()
        serialized = MessageSerializer(queryset, many=True)

        return Response(serialized, status=status.HTTP_200_OK)

    def filter_queryset(self, queryset: QuerySet) -> QuerySet:
        if self.action == 'list':
            limit = self.request.data.get('limit')
            offset = self.request.data.get('offset')

            return super().filter_queryset(queryset)[offset: offset + limit]
