from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) :
    return HttpResponse("Hello, World") 

#Adding a new function named by Ashutosh
def Ashutosh(request) :
    return HttpResponse("Hello , Ashutosh!")