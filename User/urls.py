from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path("signup/", views.sign_up, name='sign_up'),
    path("sendmail/", views.send_mail, name='send_mail'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
]
