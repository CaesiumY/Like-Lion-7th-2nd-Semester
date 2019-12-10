from rest_framework import viewsets
from .serializers import essaySerializer, albumSerializer, fileSerializer
from .models import EssayModel, AlbumModel, FileModel
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


class albumViewSet(viewsets.ModelViewSet):
    queryset = AlbumModel.objects.all()
    serializer_class = albumSerializer

    def perform_create(self, serializer):
        serializer.save(auth=self.request.user)


class fileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = fileSerializer

    def perform_create(self, serializer):
        serializer.save(auth=self.request.user)
