from django.db.models import QuerySet
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.serializers.user import UserSerializer
from core.models import User


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = AllowAny

    def create(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email is None or password is None:
            Response({'Message': "Missing required params"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if User.objects.all():
            Response({'Message', "User with such email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        user = serializer.save()

        return Response(user, status=status.HTTP_201_CREATED)

    def filter_queryset(self, queryset: QuerySet) -> QuerySet:
        if self.action == 'create':
            email = self.request.data.get('email')
            return super().filter_queryset().filter(email=email)
