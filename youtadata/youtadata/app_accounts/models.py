from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from app_base.models import Course

User = get_user_model()
EDUCATION_TYPE = (
    (1, 'دانش آموز'),
    (2, 'دیپلم'),
    (3, 'کاردانی'),
    (4, 'کارشناسی'),
    (5, 'کارشناسی ارشد'),
    (6, 'دکترا')
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    _education = models.PositiveSmallIntegerField(choices=EDUCATION_TYPE, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True)
    # birth_date = models.DateField(null=True, blank=True)
    @property
    def education(self):
        return EDUCATION_TYPE[self.education]
    @education.setter
    def eduction(self, education_type):
        reversed_type = {v:k for k, v in dict(EDUCATION_TYPE).items()}
        self._education = reversed_type.get(education_type)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class RegisteredCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' %(self.user.username, self.course.title)