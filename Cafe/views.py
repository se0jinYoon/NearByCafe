from django.shortcuts import render,redirect
from Cafe.models import *
from django.http.request import HttpRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json,math
from Review.models import *

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
    
    #리뷰가 cafe_id를 가지고 있고
    #나의 cafe_id를 가진 리뷰를 가져오면 all_review
    #all_review=cafe.review_set.all()
    
    #리뷰 관련 코드

    #all_review=cafe.cafeid_set.all()
    
    all_review=cafe.cafe_id.all()
    review_cnt=0
    sum_star=0
    average_star=0
    for review in all_review:
        review_cnt+=1
        sum_star+=review.star
    
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

    
    
    