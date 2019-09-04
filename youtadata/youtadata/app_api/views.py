from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from app_base.models import Course, CourseSession, CourseSessionExercise
from django.conf import settings

@api_view(['POST'])
@login_required
def like(request):
    obj_id = request.POST.get('id')
    obj_type = request.POST.get('type')
    if obj_id and obj_type:
        if obj_type in settings.ALLOWED_LIKE_TYPES:
            model = eval(obj_type)
            my_obj = model.objects.get(id=obj_id)
            if (my_obj.likes.filter(user=request.user)):
                my_obj.likes.filter(user=request.user ).delete()
                return Response({"message": "%s دیسلایک شد!" %my_obj.title}, status=status.HTTP_200_ok)
            else:
                my_obj.likes.create(user=request.user)
                return Response({"message": "%s لایک شد!!" %my_obj.title}, status=status.HTTP_200_ok)
    return Response({"message": "something went wrong please chek your entry"}, status=status.HTTP_200_ok)