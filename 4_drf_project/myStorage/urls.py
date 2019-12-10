from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import essayViewset, albumViewSet, fileViewSet
import rest_framework.urls

router = DefaultRouter()
router.register('essay', essayViewset)
router.register('image', albumViewSet)
router.register('file', fileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(rest_framework.urls))
]
