from django.contrib import admin
from app_base.models import (
    Course, 
    SessionCourse,
    SessionExercise,
    AttachmentsFiles)

admin.site.register(Course)
admin.site.register(SessionCourse)
admin.site.register(SessionExercise)
admin.site.register(AttachmentsFiles)
