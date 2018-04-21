# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    """
    博客分类
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    博客文章
    """
    title = models.CharField(max_length=70)
    body = models.TextField()
    excerpt = models.CharField(max_length=200, blank=True)  # 摘要
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User)
