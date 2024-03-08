from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import NutriViewSet

router = DefaultRouter()
router.register(prefix="nutri", viewset=NutriViewSet)


urlpatterns = [
    path("api/", include(router.urls))
]
