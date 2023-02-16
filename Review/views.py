
from rest_framework.response import Response
from .models import Review
from rest_framework.views import APIView
from .serializers import ReviewSerializer
from django.shortcuts import render,redirect
from Review.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from Review.forms import ReviewForm
import json
class ReviewListAPI(APIView):
    def get(self, request):
        queryset = Review.objects.all()
        print(queryset)
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)


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
    keywords = ReviewListAPI.get()

@csrf_exempt
@login_required(login_url='User:login')
def review_create(request):
    if request.method == 'POST':
        ctx = {}
        req = json.loads(request.body)
        # print(request.POST['title'])
        form = ReviewForm(req)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_id = request.user
            review.cafe_id = Cafe.objects.get(pk=1)
            # review.cafe_id = Cafe.objects.get(pk=pk)
            review.save()

        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)
            print("failed")
            ctx = {
                'form':form,'keyword_list' : keyword_list
            }
            return render(request,"review_create.html",ctx)
        return redirect('Cafe:main')
 
    else :
        return render(request,"review_create.html",{"keyword_list" : keyword_list})