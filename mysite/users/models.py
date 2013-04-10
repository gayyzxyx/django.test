from django.db import models
# -*- coding:utf-8 -*-
# Create your models here.
#每个模型相当于一个数据库表
class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
#没有申明主键，那么django会生成一个自增长的主键字段，每个模型都要求有单独的主键id
class Book(models.Model):
    title = models.CharField(max_length=100)
    #一对多的关系，django创建了一个额外的表（多对多连接表）来处理这种关系
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

#python manage.py sqlall users，也即是上面的一对多关系。sqlall命令不会创建数据库，只是把表结构打出来，我们可以手动创建也可以管道操作python manager.py sqlall users|psql mydb
#还有更简单的命令python manager.py syncdb(此命令是安全的，就算重复执行也不会重复创建表)