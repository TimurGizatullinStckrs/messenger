from rest_framework import serializers

from core.models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        depth = 1
        fields = ['pk, users']
        extra_kwargs = {'users': {'manu': True}}

    def get_last_message(self) -> Message:
        return Message.objects.filter(chat=self.pk)[-1]
