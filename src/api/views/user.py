from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

from api.serializers.user import UserSerializer
from core.models import User


class UserViewSet(viewsets.GenericViewSet):
    permission_classes = IsAuthenticated

    def retrieve(self, request, email: str):
        queryset = User.objects.all()
        user_object = get_object_or_404(queryset, email__contains=email)
        serialized = UserSerializer(user_object)

        return Response(serialized, status=status.HTTP_200_OK)

