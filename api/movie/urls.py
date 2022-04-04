from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, PersonViewSet


router = DefaultRouter(trailing_slash=True)

router.register('movie', MovieViewSet, basename='movie')
router.register('person', PersonViewSet, basename='person')

urlpatterns = [
    path('', include(router.urls)),
]