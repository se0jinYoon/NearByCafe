from django.shortcuts import render,redirect
from models import *
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
