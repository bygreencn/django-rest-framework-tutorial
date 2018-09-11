from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from backend.views import UserViewSet
from rest_framework import renderers

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from backend import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
]