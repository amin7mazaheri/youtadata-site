from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path('', views.profile, name='profile'),
]  