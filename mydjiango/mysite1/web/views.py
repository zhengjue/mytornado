# _*_ coding:utf-8 _*_
from django.shortcuts import render, render_to_response, redirect
from django.db import models


# Create your views here.

def login(request):
    ret = {"status": ""}
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        is_empty = all([username, password])
        if is_empty:
            count = models.UserInfo.objects.filter(username=username, password=password).count()
            if count == 1:
                return redirect("/web/index/")
            else:
                ret["status"] = "用户名或密码错误"
        else:
            ret["status"] = "用户名或密码为空"

        return render_to_response("login.html", ret)
