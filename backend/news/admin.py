from django.contrib import admin
from .models import *
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'status')
    fields = ('title', 'description', 'summary', 'pub_date', 'status')
admin.site.register(News)
admin.site.register(Author)
admin.site.register(Image)
