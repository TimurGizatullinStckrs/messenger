from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import ChatSerializer
from core.models import Chat


class ChatViewSet(viewsets.GenericViewSet):
    permission_classes = IsAuthenticated

    def list(self, request):
        queryset = Chat.objects.all().filter(user__contains=request.user.pk)
        serialized = ChatSerializer(queryset, many=True)
        return Response(serialized, status=status.HTTP_200_OK)
