from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_tags, name='generate_tags')
]