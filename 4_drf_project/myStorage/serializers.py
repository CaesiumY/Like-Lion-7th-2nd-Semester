from .models import EssayModel
from rest_framework import serializers


class essaySerializer(serializers.ModelSerializer):

    class Meta:
        model = EssayModel
        fields = '__all__'
