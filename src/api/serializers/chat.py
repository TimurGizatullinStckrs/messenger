from rest_framework import serializers

from core.models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    users = serializers.ManyRelatedField()
    penultimate_message = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = ['pk', 'users', 'last_message']
        depth = 1

    def get_penultimate_message(self) -> Message:
        return Message.objects.filter(chat=self.pk)[-1]
