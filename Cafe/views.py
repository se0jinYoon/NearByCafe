from django.shortcuts import render,redirect
from Cafe.models import *
from django.http.request import HttpRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def main_keyword_list(request, *args, **kwargs):
    cafe_keyword = CafeKeyword.cafe_temp
    context = {
            'keyword_list' : cafe_keyword,
        }
    return JsonResponse(context)


def main_page(request, *args, **kwargs):
    # 위치 키워드 전처리
    location_list = list(Location.Locations)
    pre_location_list_left = location_list[0:12]
    pre_location_list_right = location_list[12:]

    location_list_left = []
    location_list_right = []

    for i in range(len(pre_location_list_left)) :
        location_list_left.append(pre_location_list_left[i][0])

    for i in range(len(pre_location_list_right)) :
        location_list_right.append(pre_location_list_right[i][0])

    # 카페 키워드 전처리
    keyword_list = list(CafeKeyword.CAFE_KEYWORDS)
    pre_keyword_list_left = keyword_list[:8]
    pre_keyword_list_right = keyword_list[8:]

    keyword_list_left = []
    keyword_list_right = []

    for i in range(len(pre_keyword_list_left)) :
        keyword_list_left.append(pre_keyword_list_left[i][0])
    
    for i in range(len(pre_keyword_list_right)) :
        keyword_list_right.append(pre_keyword_list_right[i][0])

    context = {
        "location_list_left" : location_list_left,
        "location_list_right" : location_list_right,
        "keyword_list_left" : keyword_list_left,
        "keyword_list_right" : keyword_list_right,
    }


    return render(request,"mainpage.html", context=context)