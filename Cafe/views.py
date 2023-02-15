from django.shortcuts import render,redirect
from Cafe.models import *
from django.http.request import HttpRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class location:
   def __init__(self,name,lat,lng):
    self.name = name
    self.lat = lat
    self.lng = lng


location_dict = {'왕십리' : [37.56122596158312,127.03430549372456],
'강남':[37.49766189275592 , 127.02829414076893],
'건대':[37.53945064514514,127.0707408606652],
'서울대':[37.480482246689576, 126.95181374421041],
'동작':[37.49804283076126, 126.98563799296839],
'노량진':[37.513022816640365,126.9432870154441],
'구로':[37.503177063791,126.88453062451542],
'목동/양천':[37.52784583486552,126.86675357877786],
'광운대':[37.623248712464395,127.06054605501177],
'수유':[37.63783923564135,127.0264551328912],
'김포공항':[37.56599532536502,126.82612996276936],
'서울전체(용산)':[ 37.52986223233116, 126.96586726417681]
}






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
        'latitude':location_dict[location][0],
        'longtitude':location_dict[location][1],
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


