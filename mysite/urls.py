"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# include()
# 函数 include() 允许引用其它 URLconfs。
# 每当 Django 遇到 :func：~django.urls.include 时，它会截断与此项匹配的 URL 的部分，并将剩余的字符串发送到 URLconf 以供进一步处理

# path()
# path()函数有四个参数，两个必须是route,view, 两个可选参数：kwargs, name.
# route: 是一个匹配 URL 的准则,这些准则不会匹配 GET 和 POST 参数或域名.如：https://www.baidu.com/myapp/?page=12 只会尝试匹配：myapp/
# view: 当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入
# kwargs: 任意个关键字参数可以作为一个字典传递给目标视图函数
# name: 为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式

urlpatterns = [
    path('admin/', admin.site.urls),
		path('polls/', include('polls.urls'))
]
