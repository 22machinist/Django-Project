from django.shortcuts import render
from django import forms
tasks = ["Foo" , "Harry" , "George"]         #Defining the universal variable
# Create your views here.

#Adding a class to contain form
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task : ")

def index(request):
    return render(request , "tasks/index.html" , {
        "tasks" : tasks
    })


#Adding new function to add the new lists
def add (request):
    return render (request , "tasks/add.html" , {
        "form" : NewTaskForm()
    })
