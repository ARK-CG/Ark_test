from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    '''
    記事の内容を管理するクラスと思われる。

    modelの定義はここに詳しく書いてある。
    https://docs.djangoproject.com/ja/1.11/ref/models/fields/
    '''
    #タイトル
    title = models.CharField(max_length=250)
    #発行日
    pub_date = models.DateTimeField('date published', default=timezone.now)
    #適当な画像
    image = models.ImageField(upload_to='media/')
    #記事本文
    body = models.TextField()
    user = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE,default="0")

class News(models.Model):
    #タイトル
    title = models.CharField(max_length=250)
    #発行日
    pub_date = models.DateTimeField('date published', default=timezone.now)
    #適当な画像
    image = models.ImageField(upload_to='media/')
    #記事本文
    body = models.TextField()
    user = models.ForeignKey(User,related_name='newses',on_delete=models.CASCADE,default="0")

class Idea(models.Model):
    #タイトル
    title = models.CharField(max_length=250)
    #発行日
    pub_date = models.DateTimeField('date published', default=timezone.now)
    #記事本文
    body = models.TextField()

    user = models.ForeignKey(User,related_name='ideas',on_delete=models.CASCADE,default="0")