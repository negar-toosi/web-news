from django.urls import path, include
from .views import *

urlpatterns = [
    path('',NewsView),
    path('<int:nid>',NewsDetaileView),
]