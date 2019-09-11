from django.contrib import admin

# Register your models here.
from .models import People

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job')