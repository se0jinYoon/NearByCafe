from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path("signup/", views.sign_up, name='sign_up'),
    path("mail_notice/", views.mail_notice, name='mail_notice'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
]
