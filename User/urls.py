from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path("find_pw/",views.findpw_page,name="find_pw"), 
    path("signup/", views.sign_up, name='sign_up'),
    path("sendmail/", views.mail_notice, name='mail_notice'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
]

