from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"base.html")

def about(request):
    return HttpResponse( "hello from django about")

def contact(request):
    return HttpResponse( "hello from django contact")

