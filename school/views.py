from django.shortcuts import render
from  .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

def Student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    Serializer = StudentSerializer(stu)
    return JsonResponse(Serializer.data)
