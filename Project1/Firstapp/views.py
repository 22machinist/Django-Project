from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request ,"Firstapp/index.html" ) 

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

#Now we will add the function that will greet everyone who enters his name 
def greet(request , name):
    return render (request , "Firstapp/greet.html")