from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import essayViewset

router = DefaultRouter()
router.register('essay', essayViewset)

urlpatterns = [
    path('', include(router.urls))
]
