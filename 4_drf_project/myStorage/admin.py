from django.contrib import admin
from .models import EssayModel, AlbumModel, FileModel

# Register your models here.
admin.site.register(EssayModel)
admin.site.register(AlbumModel)
admin.site.register(FileModel)
