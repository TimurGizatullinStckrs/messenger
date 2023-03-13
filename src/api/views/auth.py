from django.contrib.auth import authenticate, login
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = AllowAny

    def create(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email is None or password is None:
            return Response({'Message': "Missing required params"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)

        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response(status=status.HTTP_404_NOT_FOUND)

        login(request, user)
        return Response(status=status.HTTP_200_OK)
    