from django.db import models
from django.conf import settings
# Create your models here.


class EssayModel(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()


class Album(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    images = models.ImageField(upload_to='images')
    summary = models.CharField(max_length=100)


class File(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    files = models.FileField(blank=False, null=False, upload_to='files')
    summary = models.CharField(max_length=100)
