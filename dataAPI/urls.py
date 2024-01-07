
from rest_framework.routers import DefaultRouter
from .views import get_complaint
from django.urls import path,include

urlpatterns = [
    path('api/complaint/', get_complaint, name='get_complaint'),
]