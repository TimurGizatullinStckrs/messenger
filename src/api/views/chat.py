from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import ChatSerializer
from core.models import Chat


class ChatViewSet(viewsets.GenericViewSet):
    def list(self, request):
        if not request.user.is_authenticated:
            return Response("User unauthorized", status=401)

        queryset = Chat.objects.all().filter(user__contains=request.user.pk)
        serialized = ChatSerializer(queryset, many=True)
        return Response(serialized, status=200)
