from django.shortcuts import render
from app_base.models import Course
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
def home(request):
    ctx = {}
    ctx['courses'] = Course.objects.all()
    return render(request, 'home.html', ctx)

def course_detail(request, id ):
    """
    In this view we intend to show the detail of our courses
    """
    ctx = {}
    ctx['course'] = course = Course.objects.get(id=id)
    ctx['courses'] = Course.objects.all().exclude(id=id)
    return render(request, 'course-detail.html', ctx)

def course_session_detail(request, course_id, session_id):
    """
    In this view we intend to show the detail of our courses
    """
    ctx = {}
    # import ipdb;ipdb.set_trace()
    course = Course.objects.get(id=course_id)
    ctx['session'] = course.sessioncourse_set.get(id=session_id)
    return render(request, 'course-session-detail.html', ctx)

    
@login_required
def register_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if course not in [rc.course for rc in request.user.registeredcourse_set.all()]:
        request.user.registeredcourse_set.create(course=course)
        messages.success(request, 
            ' % s عزیز شما قبلا در این دوره ثبت نام کرده اید' % request.user.username)
    else:    
        messages.add_message(request, messages.SUCCESS, 
            '%s عزیز دوره مورد نظر شما با موفقیت ثبت نام شد'%request.user.username)
    return HttpResponseRedirect(reverse('app-accounts:profile')) 
    
