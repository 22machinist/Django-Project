from django.shortcuts import render

tasks = ["Foo" , "Harry" , "George"]         #Defining the universal variable
# Create your views here.

def index(request):
    return render(request , "tasks/index.html" , {
        "tasks" : tasks
    })


#Adding new function to add the new lists
def add (request):
    return render (request , "tasks/add.html" )
