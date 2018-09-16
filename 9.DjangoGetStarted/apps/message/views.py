# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import UserMessage 
def __unicode__(self):
    return u"{} ({})".format(self.name, self.dept)
# Create your views here.

def getform(request):
    """
    :param request:
    :return: render后的HttpResponse
    """
    # 3-5 查询部分
    message = None
    all_message = UserMessage.objects.all()

    # if 判断是否存在数据
    if all_message:
        # all_message是一个list，可以使用切片。
        message = all_message[0]
        # message = all_message[2:8]

    # UserMessage默认的数据管理器objects
    # 方法1 :all()是将所有数据返回成一个queryset类型(django的内置类型)
    # all_message = UserMessage.objects.all()

    # 方法2 :filter取出指定条件值，逗号代表and 必须同时满足两个条件才返回。
    # all_message = UserMessage.objects.filter(name='111', address='111')

    # 删除操作

    # all_message.delete()


    # 我们可以对于all_message进行遍历操作
    # for message in all_message:
    #     message.delete()
    #     # 每个message实际就是一个UserMessage对象（这时我们就可以使用对象的相关方法）。
    #     print message.name

    # 存储部分

    # 首先实例化一个对象
    # user_message = UserMessage()

    # 为对象增加属性

    # user_message.name = "2"
    # user_message.message = "2222"
    # user_message.address = "22"
    # user_message.email = "2@2.com"
    # user_message.object_id = "222"

    # 调用save方法进行保存
    # user_message.save()

    # html表单部分

    # 此处对应html中的method="post"，表示我们只处理post请求
    # if request.method == "POST":
    #     # 就是取字典里key对应value值而已。取name，取不到默认空
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #
    #     # 实例化对象
    #     user_message = UserMessage()
    #
    #     # 将html的值传入我们实例化的对象.
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "333"
    #
    #     # 调用save方法进行保存
    #     user_message.save()

    return render(request, 'message_form.html',{
        "my_message" : message
    })