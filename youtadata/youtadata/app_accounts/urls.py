from django.urls import path
from app_accounts import views

urlpatterns = [
    path('', views.profile, name='profile'),
]