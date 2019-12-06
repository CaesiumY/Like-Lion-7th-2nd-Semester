from rest_framework import viewsets
from .serializers import essaySerializer
from .models import EssayModel
# Create your views here.


class essayViewset(viewsets.ModelViewSet):
    queryset = EssayModel.objects.all()
    serializer_class = essaySerializer
