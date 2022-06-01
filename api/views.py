import json
from unicodedata import name
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response


from django.views.decorators.csrf import csrf_exempt



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



@csrf_exempt
def StudentCreate(request):
    if request.method == "POST":
        data=request.body;
        stream=io.BytesIO(data);
        python_data=JSONParser().parse(stream);
        serializer=StudentSerializers(data=python_data);
        if serializer.is_valid():
            serializer.save();
        msg={"mag":"Data insert Successfully"};
        json_data=JSONRenderer().render(msg);
        return HttpResponse(json_data,content_type='application/json')
    error_msg=JSONRenderer().render(serializer.errors);
    return HttpResponse(error_msg,content_type='application/json')
