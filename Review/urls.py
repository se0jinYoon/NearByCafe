from django.urls import path
from . import views

app_name = "Review"

urlpatterns = [
    path('review_create/', views.review_create, name='review_create'),
]