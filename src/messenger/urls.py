from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import ChatViewSet

router = routers.DefaultRouter()
router.register(r'chats', ChatViewSet)

urlpatterns = router.urls
