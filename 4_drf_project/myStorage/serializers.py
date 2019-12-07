from .models import EssayModel
from rest_framework import serializers


class essaySerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = EssayModel
        fields = ('pk', 'title', 'body', 'author_name')
