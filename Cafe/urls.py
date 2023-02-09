from django.urls import path
from views import main_keyword_list

urlpattenrs = [
    path('keyword_list', main_keyword_list, name='keyword_list')
    ,
    
]