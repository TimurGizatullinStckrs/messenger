from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializers import ChatSerializer
from core.models import Chat


class ChatViewSet(viewsets.GenericViewSet):
    def list(self, request):
        if not request.user.is_authenticated:
            return Response("User unauthorized", status=status.HTTP_401_UNAUTHORIZED)

        queryset = Chat.objects.all().filter(user__contains=request.user.pk)
        serialized = ChatSerializer(queryset, many=True)
        return Response(serialized, status=status.HTTP_200_OK)
