from rest_framework import viewsets
from .serializers import essaySerializer
from .models import EssayModel
from rest_framework.filters import SearchFilter
# Create your views here.


class essayViewset(viewsets.ModelViewSet):
    queryset = EssayModel.objects.all()
    serializer_class = essaySerializer

    filter_backends = [SearchFilter]
    search_fields = ("title", "body")

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)

        else:
            qs = qs.none()

        return qs
