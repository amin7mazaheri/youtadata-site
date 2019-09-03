from django.urls import path
from app_api import views
from rest_framework.authtoken import views as auth_view


urlpatterns = [
    path('token/', auth_view.obtain_auth_token),
    path('like/', views.like, name='like'),
]