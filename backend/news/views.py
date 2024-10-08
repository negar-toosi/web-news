from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .models import *
from .serializers import *

def NewsView(request):
    if request.method == 'GET':
        news = News.objects.all()
        # image = Image.objects.filter(news=news.id)
        # print(image)
        serializers = NewsSerializer(news, many = True)
        return JsonResponse(serializers.data, safe = False)

def NewsDetaileView(request,nid=None):
    if request.method == 'GET':
        news = get_object_or_404(News,pk=nid)
        serializers = NewsDetaileSerializer(news)
    return JsonResponse(serializers.data, safe = False)

