from rest_framework import serializers
from api_messages.models import Message
import re


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('email', 'body', 'created', 'updated')

    def validate(self, data):
        if not re.match(r'^.{1,99}$', data['body']):
            raise serializers.ValidationError({
                'error': 'message body length from 1 to 99 characters'
            })
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', data['email']):
            raise serializers.ValidationError({
                'error': 'invalid email format'
            })
        else:
            return data
