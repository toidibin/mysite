from django.contrib import admin

#向管理页面中加入投票应用
# Register your models here.
from .models import Question
admin.site.register(Question)