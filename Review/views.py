from django.shortcuts import render

from rest_framework.response import Response
from .models import Review
from rest_framework.views import APIView
from .serializers import ReviewSerializer
class ReviewListAPI(APIView):
    def get(self, request):
        queryset = Review.objects.all()
        print(queryset)
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)