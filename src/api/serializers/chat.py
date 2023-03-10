from rest_framework import serializers

from core.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    users = serializers.ManyRelatedField()
    last_message = serializers.CharField()

    class Meta:
        model = Chat
        fields = ['id', 'users', 'last_message']
        depth = 1
