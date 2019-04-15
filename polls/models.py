import datetime  # 标准库中的datetime 模块
from django.db import models
from django.utils import timezone
# Create your models here.


# 模型是真实数据的简单明确的描述。它包含了储存的数据所必要的字段和行为
# Django 遵循 DRY Principle 。它的目标是你只需要定义数据模型，然后其它的杂七杂八代码你都不用关心，它们会自动从模型生成


# 每个模型被表示为 models.Model 类的子类
# 表名默认：应用名+模型名字 如： polls_question
# 主键（IDs)被默认自动创建
# 默认Django在外键字段名后追加字符串"_id" 如：question_id

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	# 自定义方法
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	# 打印一个类的时候，print首先调用的是类里面定义的__str__
	def __str__(self):
		return self.question_text


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE) # 每个 Choice 对象都关联到一个 Question 对象
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text