from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path("find_pw/",views.find_pw,name="find_pw"),
    #path("find_pw/",views.find_pw2,name="find_pw2"),
    
]