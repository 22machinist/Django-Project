from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) :
    return HttpResponse("Hello, World") 

#Adding a new function named by Ashutosh
def Ashutosh(request) :
    return HttpResponse("Hello , Ashutosh!")

#Now we will add more functions
def David(request):
    return HttpResponse("Hello , David!")

def Malan(request):
    return HttpResponse("Hello , Malan")

def Brian(request):
    return HttpResponse("Hello , Brian!")

def Havard(request):
    return HttpResponse("Hello , Harvard!")

def Mi (request):
    return HttpResponse("Hello , Mi!")