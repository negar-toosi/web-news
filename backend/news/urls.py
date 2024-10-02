from django.urls import path, include
from .views import NewsView

urlpatterns = [
    path('',NewsView),
]