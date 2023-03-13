from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.serializers.user import UserSerializer
from core.models import User


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = IsAuthenticated

    def list(self, request):
        queryset = User.objects.all()
        paginated_queryset = super().paginate_queryset(queryset)
        serialized = UserSerializer(paginated_queryset, many=True)

        return Response(serialized, status=status.HTTP_200_OK)
