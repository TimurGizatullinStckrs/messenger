from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = User
        fields = ['pk', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
