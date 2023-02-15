from django.urls import path
from . import views

app_name = "User"

urlpatterns = [

    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path("findpw/", views.findpw, name="findpw"),
    path("signup/", views.sign_up, name='sign_up'),
    path('sendmail/<str:user_name>/<str:user_email>/',
         views.mail_notice, name='mail_notice'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
    path('withdrawal/', views.delete_user, name='withdrawal'),
    path('profile', views.profile, name='profile'),
]
