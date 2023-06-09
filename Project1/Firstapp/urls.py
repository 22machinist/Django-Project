from django.urls import path    #This will import path 
from . import views             #This will import views from the current directory 
urlpatterns = [
    #Defining the path that will be rendered on the request
    path("",views.index, name="index")
]