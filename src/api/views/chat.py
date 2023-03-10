from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import ChatSerializer
from core.models import Chat


class ChatViewSet(viewsets.GenericViewSet):
    def list(self, request):
        if not request.user.is_authenticated:
            return Response("User unauthorized", status=401)

        queryset = Chat.objects.all().filter(zones__id=request.user.pk)
        serialized = ChatSerializer(queryset, many=True)
        return Response(serialized, status=200)

    def create(self, request):
        if not request.user.is_authenticated:
            return Response("User unauthorized", status=401)

        user_id = request.data.get('user_id', None)

        if not user_id:
            return Response({'Message': "Missing required arguments (user_id)"}, 400)

        chats = (
            Chat.objects.all()
            .filter(users__contains=[request.user.pk, user_id])
            .filter(is_dialog=True)
        )

        if chats:
            return Response({'Message': "Chat already exists"}, 400)

        serializer = ChatSerializer(data=request.data)
        chat = serializer.save()

        return Response(chat, status=201)