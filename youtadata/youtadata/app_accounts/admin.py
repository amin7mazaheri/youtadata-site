from django.contrib import admin
from app_accounts import models

admin.site.register(models.Profile)
admin.site.register(models.RegisteredCourse)

