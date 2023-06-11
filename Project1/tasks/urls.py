from django.urls import path 
from . import views

urlpatterns = [
    path("" , views.index , name="index") ,
    #Adding the path for add function
    path("add" , views.add , name="add")
]