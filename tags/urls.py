from django.urls import path
from . import views

urlpatterns = [
    path('api_success/', views.api_success)
]