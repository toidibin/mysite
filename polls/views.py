from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Django 中的视图的概念是「一类具有相同功能和模板的网页的集合」
# 在 Django 中，网页和其他内容都是从视图派生而来。每一个视图表现为一个简单的 Python 函数

def index(request):	
	return HttpResponse('hello, world')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)