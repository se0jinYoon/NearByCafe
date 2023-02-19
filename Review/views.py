
from .models import Review

from django.shortcuts import render,redirect
from Review.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from Review.forms import ReviewForm
import json
from collections import Counter



keyword_list=[
    '데이트',
    '작업하기 좋은',
    '공부하기 좋은',
    '조용한',
    '시끌벅적한',
    '의자가 편한',
    '디저트 맛있는',
    '커피가 맛있는',
    '친절한',
    '혼카페',
    '장소가 넓은',
    '콘센트가 많은',
    '화장실 깨끗한',
    '인테리어 예쁜',  
    ]
def insert_cafe(request,pk):
    cafe = Cafe.objects.get(id = pk)
    # keywords = ReviewListAPI.get()

@csrf_exempt
@login_required(login_url='User:login')
def review_create(request,pk):

    # 카페 객체 추가
    cafe_obj = Cafe.objects.get(id=pk)

    if request.method == 'POST':
        print("post")
        ctx = {}
        req = json.loads(request.body)
        review = Review()
        review.user_id = request.user
        review.title = req['title']
        review.content = req['content']
        review.star = req['star']
        #review.keywords = req['keywords']
        review.cafe_id = Cafe.objects.get(pk=pk)
        
        review.save()
        
        #카페 평균 별점 계산(카페상세->리뷰등록 이동)
        all_review=cafe_obj.cafe_id.all()
        review_cnt=0
        sum_star=0
        average_star=0
        for review in all_review:
            review_cnt+=1
            sum_star+=review.star
            
        if review_cnt==0:average_star==0
        else:
            average_star=sum_star/review_cnt
            print(sum_star,review_cnt,average_star)
            
        
        cafe_obj.average_star=round(average_star,1)
        #cafe_obj.average_star=average_star
        cafe_obj.save()
        

        #리뷰의 키워드(review의 keywords)를 카운트해서 카페 키워드(cafe의 keywords)로 보내주기
        
        # cnt=Counter(review.keywords)
        # if cnt>=3:
        #     x=cnt.most_common(3)
        # else:x=cnt.most_common(len(cnt))

        # for key in x.itmes():
        #     cafe_keywords.append(key)
        
        #seleted_keywords=req['seleted_ck']#선택된 키워드 리스트
        #review에서 keywords 리스트 가져와서 필터링
        #cafes=[]
            # for cafe in cafes_objects:
            #     # cafe의 리뷰에서 keywords를 가져와서 selected_keywords랑비교
            #     cafe_keywords=cafe.keywords
            #     #cafe_keywords랑 selected_keywords 비교
            #     same=[i for i,j in zip(seleted_keywords,cafe_keywords) if i==j]
                
            #     if len(same)>=2:
            #         cafes.append(cafe)
        
        


        #리뷰키워드 cafe키워드에 추가
        k_list=req['keywords']
        
        review.keywords=json.dumps(k_list,ensure_ascii=False)    
        cafe_obj.keywords=json.dumps(k_list,ensure_ascii=False)
        review.save()
        cafe_obj.save()
        
        #cafe_keywords=jsonDec.decode(cafe.keywords)
    
        #리뷰등록을 할때 키워드를 보고 카페의 키워드 체크 리스트에서 몇갠지 세고 가장 많은 이름의 것을 카페한테
        #cafe_keywords_cnt=[0]*15#튜플로 넣어놔서 같은 키워드 이름인거 의 cnt++해서 가장 많은거를 카페의cnt로?
        #jsonDec=json.decoder.JSONDecoder()
        #for r in all_review:
        #    r_list=jsonDec.decode(r.keywords)
        
        #jsonDec=json.decoder.JSONDecoder()
        #cafe_keywords=jsonDec.decode(review.cafe_id.keywords)
        #cafe_keywords=jsonDec.decode(cafe_obj.keywords)
        
        return redirect('Cafe:main')
 
    else :
        
        return render(request,"review_create.html",{"keyword_list" : keyword_list, "pk" : pk, "cafe":cafe_obj})