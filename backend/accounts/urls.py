from django.urls import path, include
from .views import *

urlpatterns = [
    path('register',RegisterView.as_view()),
    path('register/author',AuthorRegisterView.as_view()),
    
    # path('login'),
    # path('logout'),
     
]