# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
 
 
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name="blog_posts")
    # related_name="blog_posts"作用是允许User反向查询到BlogArticles
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
 
    class Meta:
        ordering = ("-publish",)
        verbose_name = "文章列表"
        verbose_name_plural = verbose_name
    # BlogArticles示例对象的显示顺序，按照publish的字段值倒叙显示
    
    # def __str__(self):
    #    return self.title   #support python3


    def __unicode__(self):
        return self.title    