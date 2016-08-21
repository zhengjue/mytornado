# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from app01 import models
import json
import datetime

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            current_user_obj = models.Admin.objects.get(username=username, password=password)
        except Exception, e:
            current_user_obj = None

        if current_user_obj:
            request.session['current_user_id'] = current_user_obj.id
            return redirect("/app01/index/")
        else:
            return render_to_response("login.html")
    return render_to_response("login.html")


def index(request):
    all_data = models.News.objects.all()
    return render_to_response("index.html", {"data": all_data})


def addfavor(request):
    result = {"status": 0, "data": "", "error": ""}
    try:
        id = request.POST.get("nid")
        obj = models.News.objects.get(id=id)
        nums = obj.favor_count + 1
        obj.favor_count = nums
        obj.save()
        result["status"] = 1
        result["data"] = nums
    except Exception, e:
        result["error"] = e.message
    return HttpResponse(json.dumps(result))


class CJosnEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime.datetime):
                return obj.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(obj, datetime.date):
                return obj.strftime("%Y-%m-%d")
            else:
                return json.JSONEncoder.default(self, obj)


def getreply(request):
    id = request.POST.get("nid")
    reply_list = models.Reply.objects.filter(new__id=id).values("id", "content", "create_date", "user__username")
    reply_list = list(reply_list)
    reply_list = json.dumps(reply_list, cls=CJosnEncoder)
    return HttpResponse(reply_list)


def getchat(request):
    chat_list = models.Chat.objects.all().order_by("-id")[0:10].values("id", "content", "user__username", "create_date")
    chat_list = list(chat_list)
    chat_list = json.dumps(chat_list, cls=CJosnEncoder)
    return HttpResponse(chat_list)


def getchat2(request):
    last_id = request.POST.get("last_id")
    chat_list = models.Chat.objects.filter(id__gt=last_id).values("id", "content", "user__username", "create_date")
    #  print type(chat_list), chat_list
    chat_list = list(chat_list)
    chat_list = json.dumps(chat_list, cls=CJosnEncoder)
    #  print chat_list
    return HttpResponse(chat_list)


def addmsg(request):
    result = {"status": 0, "data": "", "error": ""}
    try:
        values = request.POST.get("data")
        userobj = models.Admin.objects.get(id=request.session["current_user_id"])
        chatobj = models.Chat.objects.create(content=values, user=userobj)
        result["status"] = 1
        result["data"] = {"username": userobj.username,
                          "id": chatobj.id,
                          "create_date": chatobj.create_date.strftime("%Y-%m-%d %H:%M:%S")}
        #  print chatobj.id
    except Exception, e:
        result["error"] = e.message
    return HttpResponse(json.dumps(result))


def addreply(request):
    result = {"status": 0, "data": "", "error": ""}
    try:
        id = request.POST.get("nid")
        data = request.POST.get("data")
        newobj = models.News.objects.get(id=id)
        userobj = models.Admin.objects.get(id=request.session["current_user_id"])
        obj = models.Reply.objects.create(content=data, user=userobj, new=newobj)
        temp = newobj.reply_count + 1
        newobj.reply_count = temp
        newobj.save()

        result["data"] = {"content": obj.content, "user_username": obj.user.username, "reply_count": temp,
                          "id": obj.id, "create_date": obj.create_date.strftime("%Y-%m-%d %H:%M:%S")}
        result["status"] = 1
    except Exception, e:
        result["error"] = e.message
    return HttpResponse(json.dumps(result))
