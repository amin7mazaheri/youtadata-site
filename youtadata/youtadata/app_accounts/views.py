from django.shortcuts import render


def profile(request):
    return render(request, 'student-dashbord.html')