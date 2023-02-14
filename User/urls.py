from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path("findpw/",views.findpw,name="findpw"), 
    path("signup/", views.sign_up, name='sign_up'),
    path("sendmail/", views.mail_notice, name='mail_notice'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
]

