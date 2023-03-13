from rest_framework import serializers

from core.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    users = serializers.ManyRelatedField()
    last_message = serializers.CharField()

    class Meta:
        model = Chat
        fields = ['pk', 'users', 'last_message']
        depth = 1
