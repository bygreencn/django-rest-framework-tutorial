# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import get_object_or_404, render

from .forms import LoginForm


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)    # get form data submitted
        if login_form.is_valid():
            cd = login_form.cleaned_data    # cd(dict)
            user = authenticate(username=cd["username"],password=cd["password"])    #return a User instance if match else None
            if user:
                login(request, user)     # execute login
                return HttpResponse("Login~Welcome~")
            else:
                return HttpResponse("Fail!Check your username or password")
        else:
            return HttpResponse("Invalid data")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})
