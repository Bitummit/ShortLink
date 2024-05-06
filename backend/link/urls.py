from django.urls import path
from .views import LinkAPIView


# app_name = "api"

urlpatterns = [
    path('links/', LinkAPIView.as_view()),
]
