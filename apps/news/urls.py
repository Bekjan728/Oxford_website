from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    NewsViewSet, 
    EventViewSet
)


router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('event', EventViewSet)


urlpatterns = [ 
]

urlpatterns += router.urls