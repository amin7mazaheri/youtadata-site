from django.contrib import admin
from django.urls import path, include
from app_base import views


urlpatterns = [
    path('', views.home, name='home'),
    path('course-detail/<int:id>/', views.course_detail, name='course-detail'),
    path('courses-<int:course_id>/session-<int:session_id>/', views.course_session_detail, name='course-session-detail'),
    path('register-course/<int:course_id>/', views.register_course, name='register-course'),
]
