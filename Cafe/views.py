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

    context = {}
    return render(request, "mainpage.html", context=context)

#q.여기서 우리가 클릭한 카페 id를 보내줘야하는데 js로 html에 바로 구겨넣었는데 그거 어케하지?
def cafe_detail(request,pk,*args,**kwargs):
    cafe=Cafe.objects(id=pk)
    
    #리뷰가 cafe_id를 가지고 있고
    #나의 cafe_id를 가진 리뷰를 가져오면 all_review
    all_review=cafe.review_set.all
    
    review_cnt=0
    for i in range(all_review):
        review_cnt+=1
    
    context={
        "cafe":cafe,
        "review_cnt":review_cnt,
           
    }
    
    #url경로 다시 지정
    return render(request,"cafe_detail.html",context=context)