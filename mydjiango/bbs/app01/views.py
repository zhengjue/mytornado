from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.core import serializers
from app01 import models
import json
import datetime

# Create your views here.


def index(request):
    all_data = models.News.objects.all()
    return render_to_response("index.html", {"data": all_data})


def addfavor(request):
    result = {"status": 0, "data": "", "error": ""}
    try:
        id = request.POST.get("nid")
        obj = models.news.objects.get(id=id)
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
                return obj.strftime("%Y-%m-%d %H%M%S")
            elif isinstance(obj, datetime.date):
                return obj.strftime("%Y-%m-%d")
            else:
                return json.JSONEncoder.default(self, obj)


def getreply(request):
    id = request.POST.get("nid")
    reply_list = models.Reply.objects.filter(new__id=id).values("id", "content", "create_date", "user__username")
    reply_list = list(reply_list)
    reply_list = json.dumps(reply_list, cls=CJosnEncoder)
    print reply_list
    return HttpResponse(reply_list)


def addreply(request):
    result = {"status": 0, "data": "", "error": ""}
    try:
        id = request.POST.get("nid")
        data = request.POST.get("data")
        new = models.news.objects.get(id=id)
        models.Reply.objects.create(content=data
                                    user=xxx,
                                    new=new)                                    )
        nums = obj.favor_count + 1
        obj.favor_count = nums
        obj.save()
        result["status"] = 1
        result["data"] = nums
    except Exception, e:
        result["error"] = e.message
    return HttpResponse(json.dumps(result))
