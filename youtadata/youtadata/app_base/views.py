from django.shortcuts import render
from app_base.models import Course

def home(request):
    ctx = {}
    ctx['courses'] = Course.objects.all()
    return render(request, 'home.html', ctx)

def course_detail(request, id ):
    """
    In this view we intend to show the detail of our courses
    """
    ctx = {}
    ctx['course'] = Course.objects.get(id=id)
    ctx['courses'] = Course.objects.all().exclude(id=id)
    return(request, 'course-detail', ctx)
