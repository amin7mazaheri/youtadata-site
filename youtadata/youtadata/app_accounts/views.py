from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_accounts.models import RegisteredCourse

@login_required
def profile(request):
    # import ipdb ; ipdb.set_trace();
    ctx = {}
    ctx['registered_course'] = [rc.course for rc in request.user.registeredcourse_set.all()]
    return render(request, 'student-dashbord.html', ctx)