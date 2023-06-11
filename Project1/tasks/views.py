from django.shortcuts import render

tasks = ["Foo" , "Harry" , "George"]         #Defining the universal variable
# Create your views here.

def index(request):
    return render(request , "tasks/index.html" , {
        "tasks" : tasks
    })
