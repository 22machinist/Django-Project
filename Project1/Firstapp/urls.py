from django.urls import path    #This will import path 
from . import views             #This will import views from the current directory 
urlpatterns = [
    #Defining the path that will be rendered on the request
    path("",views.index, name="index"),
    path("Ashutosh" , views.Ashutosh , name="Ashutosh"),
    path("David" , views.David , name="David") , 
    path("Malan" , views.Malan , name="Malan"),
    path("Brian" , views.Brian , name="Brian"),
    path("Havard" , views.Havard , name="Havard"),
    path("Mi" , views.Mi , name="Mi")
]