from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import ChatSerializer
from core.models import Chat


class ChatViewSet(viewsets.GenericViewSet):
    permission_classes = IsAuthenticated

    def list(self, request):
        queryset = Chat.objects.all()
        serialized = ChatSerializer(queryset, many=True)
        return Response(serialized, status=status.HTTP_200_OK)

    def create(self, request):
        user_id = request.data.get('user_id', None)

        if not user_id:
            return Response({'Message': "Missing required arguments (user_id)"}, status=status.HTTP_400_BAD_REQUEST)

        chats = Chat.objects.all()

        if chats:
            return Response({'Message': "Chat already exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ChatSerializer(data=request.data)
        chat = serializer.save()

        return Response(chat, status=status.HTTP_201_CREATED)

    def filter_queryset(self, queryset: QuerySet) -> QuerySet:
        if self.action == 'create':
            return (
                super().filter_queryset(queryset)
                .filter(users__cantains=[self.request.user.pk, self.request.data.get('user_id')])
                .filter(is_dialog=True))
        elif self.action == 'list':
            return super().filter_queryset(queryset).filter(user=self.request.user)
