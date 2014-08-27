# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from .api_views import (
    ContactViewSet
)
router = DefaultRouter()

router.register(
    r'/contact',
    ContactViewSet,
    'api-contact'
)

urlpatterns = router.urls
