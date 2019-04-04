**初识别一些命令行**

```python
python manage.py migrate
```

 [`migrate`](https://docs.djangoproject.com/zh-hans/2.2/ref/django-admin/#django-admin-migrate) 命令检查 [`INSTALLED_APPS`](https://docs.djangoproject.com/zh-hans/2.2/ref/settings/#std:setting-INSTALLED_APPS) 设置，为其中的每个应用创建需要的数据表，至于具体会创建什么，这取决于你的 `mysite/settings.py` 设置文件和每个应用的数据库迁移文件



```python
python manage.py makemigrations polls
```

创建好应用后，添加到 INSTALLED_APPS,DJango项目包含了该应用

通过运行makemigrations命令，Django会检测你对模型文件的修改，并且把修改的部分存储为一次迁移。

查看迁移过程的文件命令(如：0001_initial.py)：

```python
python manage.py sqlmigrate polls 0001
```

可以查看到sql语句。



再次执行migrate命令，在数据库中创建新定义的模型的数据表：

```python
python manage.py migrate
```



**改变模型的三个步骤：**

- 编辑 `models.py` 文件，改变模型。
- 运行 [`python manage.py makemigrations`](https://docs.djangoproject.com/zh-hans/2.2/ref/django-admin/#django-admin-makemigrations) 为模型的改变生成迁移文件。
- 运行 [`python manage.py migrate`](https://docs.djangoproject.com/zh-hans/2.2/ref/django-admin/#django-admin-migrate) 来应用数据库迁移。