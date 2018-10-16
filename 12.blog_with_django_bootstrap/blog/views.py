# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogArticles

def blog_title(request):
    blogs = BlogArticles.objects.all()    
    # 把Django后台数据库里BlogArticles的所有东西掏出来，先放在blogs里面
    return render(request, "blog/titles.html", {"blogs":blogs})    
    #把这个变量的值传给html里面的blogs变量（{"blogs":blogs} 中的前一个，其实这两个可以不同名)

def blog_article(request, article_id):
    # article=BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id) # 找不到就跳转到404页面
    pub = article.publish
    return render(request, 'blog/content.html', {"article": article, "publish": pub})