from django.urls import path
from . import views

app_name = "User"

urlpatterns = [
    path("signup/", views.sign_up, name='sign_up'),
    #path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
]
