from django.contrib import admin
from django.urls import path, include
from app_base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course-detail/<str:slug>/', views.course_detail, name='course-detail'),
    path('<str:course_title>/<str:session_title>/', views.course_session_detail, name='course-session-detail'),
    path('<str:course_title>/<str:session_title>/<str:exercise_title>/', views.course_session_exercise_detail, name='course-session-exercise-detail'),
    path('register-course/<int:course_id>/', views.register_course, name='register-course'),
]