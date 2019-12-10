from .models import EssayModel, AlbumModel, FileModel
from rest_framework import serializers


class essaySerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = EssayModel
        fields = ('pk', 'title', 'body', 'author_name')


class albumSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.username")
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = AlbumModel
        fields = ('pk', 'images', 'summary', 'author_name')


class fileSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.username")
    files = serializers.FileField(use_url=True)

    class Meta:
        model = FileModel
        fields = ('pk', 'files', 'summary', 'author_name')
