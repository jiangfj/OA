"""个人报告模块"""
import json
from tools.login_dec import login_check

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# from index.views import logging_check
from management.models import Management
from report.models import Report_list


# Create your views here.


@login_check
def list(request):
    if request.method == "GET":
        user = request.myuser
        all_notice = Report_list.objects.filter(user=user).order_by("-created_time")
        json0 = []
        for i in all_notice:
            json2 = {}
            json2['id'] = i.id
            json2['title'] = i.title
            json2['content'] = i.content
            json2['created_time'] = i.created_time
            json2['updated_time'] = i.updated_time
            #json2['management'] = Management.objects.get(id=i.management).dep_name
            json0.append(json2)
        return JsonResponse({"code": 200, "obj": json0})


@login_check
def add(request):
    if request.method == "POST":
        json_str = request.body
        user = request.myuser
        #management = Management.objects.get(name=user).id
        json_obj = json.loads(json_str)
        title = json_obj['title']
        content = json_obj['content']
        all_notices = Report_list.objects.all()
        lists = []
        for i in all_notices:
            uname = i.title
            lists.append(uname)
        if title in lists:
            return JsonResponse({"code": 301})
        Report_list.objects.create(title=title, content=content, user=user)
        all_notice = Report_list.objects.filter(title=title)

        print(all_notice)
        if all_notice:
            json2 = {}
            json2['title'] = all_notice[0].title
            json2['content'] = all_notice[0].content
            json2['created_time'] = all_notice[0].created_time
            json2['updated_time'] = all_notice[0].updated_time
            return JsonResponse({"code": 200, "obj": json2})
        else:
            return JsonResponse({"code": 300, 'error': "添加失败"})


@login_check
def content(request):
    if request.method == "POST":
        # 当前公告内容显示
        json_str = request.body
        json_obj = json.loads(json_str)
        id = json_obj["id"]
        try:
            notice = Report_list.objects.get(id=id)
            json2 = {}
            json2["title"] = notice.title
            json2["content"] = notice.content
            json2["updated_time"] = notice.updated_time
        except Exception as e:
            print(e)
            return JsonResponse({"code": 300, 'error': "显示失败"})
        return JsonResponse({"code": 200, "obj": json2})


@login_check
def update(request, _id=None):
    if request.method == "GET":
        json2 = {}
        try:
            notice = Report_list.objects.get(id=_id)
            json2["title"] = notice.title
            json2["content"] = notice.content
        except Exception as e:
            print(e)
        return JsonResponse({"code": 200, "obj": json2})
    elif request.method == "POST":
        json_str = request.body
        json_obj = json.loads(json_str)
        id = json_obj["id"]
        title = json_obj["title"]
        content = json_obj["content"]
        _title = json_obj["_title"]
        all_notices = Report_list.objects.all()
        lists = []
        for i in all_notices:
            if _title == i.title:
                continue
            else:
                lists.append(i.title)
        if title in lists:
            return JsonResponse({"code": 301})
        try:
            notice = Report_list.objects.get(id=id)
        except Exception as e:
            print(e)
            return JsonResponse({"code": 300})
        try:
            notice.title = title
            notice.content = content
        except Exception as e:
            print("---修改失败---")
            print(e)
        notice.save()
        return JsonResponse({"code": 200})


@login_check
def delete(request):
    if request.method == "POST":
        json_str = request.body
        json_obj = json.loads(json_str)
        id = json_obj["id"]
        try:
            notice = Report_list.objects.filter(id=id)
            notice.delete()
        except Exception as e:
            print(e)
            return JsonResponse({"code": 300})
        return JsonResponse({"code": 200})
