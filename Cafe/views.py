from django.shortcuts import render,redirect, reverse
from Cafe.models import *
from django.http.request import HttpRequest
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json,math
from Review.models import *


location_dict = {'왕십리/한양대/성수' : [37.56122596158312,127.03430549372456],
'강남/역삼/선릉/압구정':[37.49766189275592 , 127.02829414076893],
'건대입구/세종대':[37.53945064514514,127.0707408606652],
'서울대입구/신림':[37.480482246689576, 126.95181374421041],
'동작/흑석/상도':[37.49804283076126, 126.98563799296839],
'노량진/여의도/영등포/당산':[37.513022816640365,126.9432870154441],
'구로/신도림':[37.503177063791,126.88453062451542],
'목동/양천/금천':[37.52784583486552,126.86675357877786],
'광운대/공릉/노원/도봉':[37.623248712464395,127.06054605501177],
'수유/미아':[37.63783923564135,127.0264551328912],
'김포공항/염창/강서':[37.56599532536502,126.82612996276936],
'서울 전체':[ 37.52986223233116, 126.96586726417681],
'홍대/합정/망원/서강' :[37.555801113296894, 126.92495439649478],
'신촌/이대/서대문/아현':[ 37.554294814089644,126.93763112560798],
'혜화/성균관대':[37.58186370670705,127.00259258535856],
'청량리/회기':[ 37.58035852300995,127.04751467848493],
'성신여대/안암/성북/길음':[37.59229597707164,127.01721082858734],
'잠실/송파/강동':[ 37.5135067680033,127.10106376984062],
'을지로/명동/중구':[37.56092381888689,126.98636161215958],
'서초/교대/사당':[ 37.49354668637486,127.01532232510674],
'종로/인사동/동대문':[ 37.57054723602707,127.0014262721575
],
'서울역/이태원/용산':[37.55437973351499,126.97071115287041],
'중랑/쌍봉':[37.59221753953163,127.07778832853602],
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
    keyword_list = list(CAFE_KEYWORDS)
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

    # 카페 검색 POST를 받았을 시
    if request.method == 'POST':
        loc = request.POST.get('cafe_location_name')
        keyword = request.POST.get('cafe_keyword_name')
        print(request.POST)
        return redirect("Cafe:find_cafe")
        
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

    print(request.GET)
    return render(request,"find_cafe.html", context=context)


@csrf_exempt
def find_cafe_ajax(request, *args, **kwargs):
    if request.method == 'POST':
        #프론트에서 넘겨줘야함! html에서 location의 문자열 보내주기
        print('get')
        req = json.loads(request.body)
        location = req['location']
        # selected_location = request.GET['location']
        selected_location = location
        cafe_location = Location.objects.get(name = selected_location)
        cafes_objects = cafe_location.cafe_set.all()
        # cafes_latlog = cafes.location.name
        #cafes=list((cafes_objects).values())
        
        #키워드 해당하는 cafes필터링
        #q1. 저 cafes첫번째꺼 변수명 바꿔도되나요?저는 객체가 필요해섭,,
        #qq. 카페키워드 가진 애 filter 변수 채우기
         
        seleted_keywords=req['seleted_ck']#선택된 키워드 리스트
        #review에서 keywords 리스트 가져와서 필터링
        cafes=[]

        for cafe in cafes_objects:

            # cafe의 리뷰에서 keywords를 가져와서 selected_keywords랑비교
            cafe_keywords=cafe.keywords
            #cafe_keywords랑 selected_keywords 비교
            same=[i for i,j in zip(seleted_keywords,cafe_keywords) if i==j]
            
            if len(same)>=2:
                cafes.append(cafe)

        context = {
        'latitude':location_dict[location][0],
        'longtitude':location_dict[location][1],
        'cafes':cafes,
        }
        
 
    return JsonResponse(context=context)

    
    
    