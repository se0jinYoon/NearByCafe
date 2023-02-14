from django.shortcuts import render,redirect
from Cafe.models import *
from django.http.request import HttpRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json,math
from Review.models import *

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

#q.여기서 우리가 클릭한 카페 id를 보내줘야하는데 js로 html에 바로 구겨넣었는데 그거 어케하지?
# <a href="{% url 'Cafe:cafe_detail' post.pk %}">{{post.title}}</a></p>
# 카페 찾기(지도)랑 연결 후 수정
def cafe_detail(request,pk,*args,**kwargs):
    cafe=Cafe.objects.get(id=pk)
  
    #카페에 등록된 리뷰들 불러오기
    all_review=cafe.cafe_id.all()
    review_cnt=0
    sum_star=0
    average_star=0
    for review in all_review:
        review_cnt+=1
        sum_star+=review.star
        
        #학교인증마크 획득
        if school_match(review.user_id.email_address,cafe.location_id.name):
            review.mark=True
        else:review.mark=False
        review.save()
    average_star=sum_star/review_cnt
    
    r_average_star=round(average_star)
    
    cafe.average_star=average_star
    cafe.save()
    
    
    
    context={
        "cafe":cafe,
        "review_cnt":review_cnt,
        "all_review":all_review,
        "r_average_start":r_average_star,
           
    }
    
    return render(request,"cafe_detail_cj.html",context=context)

def school_match(cafe_location,user_school_email):
    school_to_location=[
        {'g.hongik.ac.kr':'신촌/이대/서대문/아현'},
        {'smu.kr','종로/인사동/동대문'},
        {'ewhain.net','신촌/이대/서대문/아현'},
        {'khu.ac.kr','청량리/회기'},
        {'hufs.ac.kr','청량리/회기'},
        {'yonsei.ac.kr','신촌/이대/서대문/아현'},
        {'duksung.ac.kr','광운대/공릉/노원/도봉'},
        {'sju.ac.kr','건대입구/세종대'},
        {'uos.ac.kr','청량리/회기'},
        {'dongduk.ac.kr','성신여대/안암/성북/길음'},
        {'kookmin.ac.kr','성신여대/안암/성북/길음'},
        {'snu.ac.kr','서울대입구/신림'},
        {'sungshin.ac.kr','성신여대/안암/성북/길음'},
        {'kw.ac.kr','광운대/공릉/노원/도봉'},
        {'konkuk.ac.kr','건대입구/세종대'},
        {'korea.ac.kr','성신여대/안암/성북/길음'},
        {'hanyang.ac.kr','왕십리/한양대/성수'},
        {'catholic.ac.kr','서초/교대/사당'},
        {'sogang.ac.kr','신촌/이대/서대문/아현'},
        {'cau.ac.kr','동작/흑석/상도'},
        { 'skku.edu','혜화/성균관대'},]
    
    for key in school_to_location:
        if key==user_school_email:
            cafe_location==school_to_location[key]
            return True
    return False
        

@csrf_exempt
def cafe_like(request):
    req=json.loads(request.body)
    like_id=req['id']
    clicked=req['clicked']
    cafe=Cafe.objects.get(id=like_id) #cafe객체
    
    #좋아요 누름
    if clicked== True:
        CafeLike.objects.create(
            cafe_id=cafe,
            user_id=request.user,
        )
        
    else:#취소 누름
        #cafe_like=cafe.cafelike_set.all
        cafe_like=cafe.cafe_like.all()
        cafe_like.delete()
        
        
    #cafe_like2=cafe.cafelike_set.all
    #cafe_like=CafeLike.objects.get(cafe_id=like_id) #cafe_like객체
    #cafe_like.num+=1
    #cafe_like.save()
    
    return JsonResponse({'id':like_id,'clicked':clicked})

    
    
    

def find_cafe(request, *args, **kwargs):
    Location_list = dict(Location.Locations)
    Location_keys = tuple(Location_list.keys())   #['서울전체', '왕십리',]
    keys_left = tuple(Location_keys[0:12])
    keys_right = tuple(Location_keys[12:])
    Location_list_left = { i : Location_list[i] for i in keys_left}
    Location_list_right = { i : Location_list[i] for i in keys_right}
    # for keyL in keys_left:
    #     Location_list_left = dict(Location_list[keyL])
    # for keyR in keys_right:
    #     Loation_list_right = dict(Location_list[keyR])

    context = {
        "location_list_left": Location_list_left,
        "location_list_right": Location_list_right
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


