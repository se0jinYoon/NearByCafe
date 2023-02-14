from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path('withdrawal/', views.delete_user, name='withdrawal')
    
]