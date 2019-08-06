from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Course(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)


class SessionCourse(models.Model):
    course =models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    attachment_files = GenericRelation('AttachmentsFiles')


class SessionExercise(models.Model):
    course_session =models.ForeignKey(SessionCourse, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    attachment_files = GenericRelation('AttachmentsFiles')


class AttachmentsFiles(models.Model):
    file = models.FileField(upload_to= 'attach_file/%y-%m-%d_%H:%M')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.content_object.title

