from django.urls import path
from .views import *   

urlpatterns = [
    path('media_upload/',ImageView.as_view())
]