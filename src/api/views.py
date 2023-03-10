from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Chat
from .serializers import ChatSerializer


class ChatViewSet(viewsets.GenericViewSet):
    def list(self, request):
        if not request.user.is_authenticated:
            return Response("User unauthorized", status=401)

        queryset = Chat.objects.all().filter(zones__id=request.user.pk)
        serialized = ChatSerializer(queryset, many=True)
        return Response(serialized, status=200)
