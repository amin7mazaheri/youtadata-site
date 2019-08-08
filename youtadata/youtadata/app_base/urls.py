from django.contrib import admin
from django.urls import path, include
from app_base import views


urlpatterns = [
    path('', views.home),
    path('course-detail/<int:id>', views.course_detail, name='course-detail'),
]