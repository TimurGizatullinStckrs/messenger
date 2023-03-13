from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializers.user import UserSerializer
from core.models import User


class AuthViewSet(viewsets.GenericViewSet):

    def sign_in(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email is None or password is None:
            Response({'Message': "Missing required params"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

