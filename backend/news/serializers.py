from rest_framework import serializers
from .models import *

class NewsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = ('id', 'title', 'summary', 'author', 'pub_date', 'image')
    def get_image(self,obj):
        image = Image.objects.filter(news=obj,main_image=True).first()
        return image.image.url

class NewsDetaileSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = ('id','title', 'description', 'author', 'pub_date','image')

    def get_image(self,obj):
        images = Image.objects.filter(news=obj)
        return [image.image.url for image in images]
