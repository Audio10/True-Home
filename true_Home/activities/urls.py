
"""Circles URLs."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views.properties import PropertyViewSet
from .views.activities import ActivityViewSet
from .views.surveys import SurveyViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='property')
router.register(
    r'properties/(?P<property_id>[^/.]+)/activities',
    ActivityViewSet,
    basename='activity'
)
router.register(
    r'activities/(?P<activity_id>[^/.]+)/surveys',
    SurveyViewSet,
    basename="survey-detail"
)

urlpatterns = [
    path('', include(router.urls))
]
