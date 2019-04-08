from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
# Create your views here.
# Django 中的视图的概念是「一类具有相同功能和模板的网页的集合」
# 在 Django 中，网页和其他内容都是从视图派生而来。每一个视图表现为一个简单的 Python 函数

#每个视图必须要做的只有两件事：返回一个包含被请求页面内容的 HttpResponse 对象，或者抛出一个异常，比如 Http404
# 你的视图可以从数据库里读取记录，可以使用一个模板引擎（比如 Django 自带的，或者其他第三方的），
# 可以生成一个 PDF 文件，可以输出一个 XML，创建一个 ZIP 文件，你可以做任何你想做的事，使用任何你想用的 Python 库


def index(request):	
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list
	}
	return render(request, 'polls/index.html', context) # 载入模板，填充上下文，再返回由它生成的 HttpResponse 对象 render快捷函数 不再需要导入loader httpResponse
	# return HttpResponse(template.render(context, request))
	# output = ', '.join([q.question_text for q in latest_question_list])
	# return HttpResponse(output)

def detail(request, question_id):
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
  # return HttpResponse("You're looking at question %s." % question_id) 1

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/result.html', {'question': question})
  # return HttpResponse(response % question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html',{
			'question': question,
			'error_message': "you didn't select a choice."
		})
	else:
		selected_choice.votes +=1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  # 想要跳转的视图的名字和该视图所对应的 URL 模式中需要给该视图提供的参数
  # return HttpResponse("You're voting on question %s." % question_id)