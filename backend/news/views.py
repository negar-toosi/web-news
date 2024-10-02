from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer

def NewsView(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializers = NewsSerializer(news, many = True)
        return JsonResponse(serializers.data, safe = False)
     