from django.urls import path
from User import views

app_name = "User"

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('profile', views.profile ,name='profile') 
]