from django.shortcuts import render
from app1.models import *
# Create your views here.
def display(request):
    response=render(request, "app1/index.html")
    return response
def display_msg(request):
    name=request.GET['name']
    email=request.GET['email']
    subject=request.GET['sub']
    message=request.GET['msg']
    s=Student(name=name, email=email, subject=subject, message=message)
    s.save()
    response=render(request,"app1/index.html", context={'msg':'Details sended Successfully....!'})
    return response