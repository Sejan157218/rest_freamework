import json
from unicodedata import name
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

from api.serializer import StudentSerializers
# Create your views here.
from api.models import Student

def UrlsPatterns(request):
    urls=[
        {
            'all_students':"api/all-students",
            'single-student':"api/student/<int:pk>",
        }
    ]
    
    return HttpResponse(urls);


    

def StudentAll(request):
    student=Student.objects.all();
    serializer=StudentSerializers(student, many=True);
    # student_json=JSONRenderer().render(serializer.data);
    # return HttpResponse(student_json,content_type='application/json');
    return JsonResponse(serializer.data,safe=False);


def SingleStudent(request,pk):
    student=Student.objects.get(roll=pk);
    serializer=StudentSerializers(student,many=False);
    student_json=JSONRenderer().render(serializer.data);
    return HttpResponse(student_json,content_type='application/json');