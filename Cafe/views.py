from django.shortcuts import render,redirect
from Cafe.models import *
from django.http.request import HttpRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

#1.지역설정
#2.키워드 설정 필터링
#3.지도에 핀 꽂기 
#  
@csrf_exempt
def main_keyword_list(request, *args, **kwargs):
    cafe_keyword = CafeKeyword.cafe_temp
    context = {
            'keyword_list' : cafe_keyword,
    } 


    return JsonResponse(context)




def main_page(request, *args, **kwargs):
    context = {}
    return render(request, "mainpage.html", context=context)




def find_cafe(request, *args, **kwargs):
    location_list = list(Location.Locations)
    pre_location_list_left = location_list[0:12]
    pre_location_list_right = location_list[12:]

    location_list_left = []
    location_list_right = []

    for i in range(len(pre_location_list_left)) :
        location_list_left.append(pre_location_list_left[i][0])

    for i in range(len(pre_location_list_right)) :
        location_list_right.append(pre_location_list_right[i][0])

    context = {
        "location_list_left" : location_list_left,
        "location_list_right" : location_list_right,
    }
    return render(request,"find_cafe.html", context=context)


@csrf_exempt
def find_cafe_ajax(request, *args, **kwargs):

    if request.method == 'POST':
        #프론트에서 넘겨줘야함! html에서 location의 문자열 보내주기
        print('get')
        req = json.loads(request.body)
        location = req['location']
        location = Location.objects.get(name=location)
        latitude = location.latitude
        longtitude = location.longtitude
        # selected_location = request.GET['location']
        selected_location = location
        cafe_location = Location.objects.get(name = selected_location)
        cafes = cafe_location.cafe_set.all()
        # cafes_latlog = cafes.location.name
        cafes=list((cafes).values())
        context = {
        'latitude':latitude,
        'longtitude':longtitude,
        'cafes':cafes,
        }
        
    # return render(request,"find_cafe.html",context=context)
        return JsonResponse(context)
    
    # return render(request, "find_cafe.html", context=context)

    #selected_location 과 같은 cafe의 location의 name을 가져와야 한다. 

    #지역에 저장된 카페를 띄우자
    #위에서 받아온 location  name 정보를 ㄱ가진 카페를 가져온다. 
    #그 애들을 컨텍스트에 담아서 html에 보내주면 html에서는 for문으로 보여준다~
    #이거를 ajax해본다...
    #cafes = cafe_location.cafe_set.all()
    #cafe_location은 selected_location과 같은 location 객체 받아옴..

    #이 카페들을 html에 보내서 for문 돌려서 출력


