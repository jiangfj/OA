"""通知公告模块"""
from django.core.paginator import Paginator
from django.shortcuts import render
from notice.models import Notice_list
from management.models import Management
from django.http import HttpResponseRedirect, JsonResponse
import json
from tools.login_dec import login_check


# Create your views here.

@login_check
def notice_list(request, json0=None):
    if request.method == "GET":
        # 全部公告列表显示
        all_notice = Notice_list.objects.all().order_by("-created_time")
        count = len(all_notice)
        json0 = []
        for i in all_notice:
            json2 = {}
            json2['id']=i.id
            json2['title'] = i.title
            json2['content'] = i.content
            json2['created_time'] = i.created_time
            json2['updated_time'] = i.updated_time
            json0.append(json2)
        return JsonResponse({"code": 200, "obj": json0})
    elif request.method == "POST":
        json_str = request.body
        json_obj = json.loads(json_str)
        name = json_obj['name']
        print(name)
        all_notice = Notice_list.objects.filter(title=name)
        print(all_notice)
        if all_notice:
            json2 = {}
            json2['title'] = all_notice[0].title
            json2['content'] = all_notice[0].content
            json2['created_time'] = all_notice[0].created_time
            json2['updated_time'] = all_notice[0].updated_time
            return JsonResponse({"code": 200, "obj": json2})

        else:
            return JsonResponse({"code": 300})


@login_check
def notice_add_view(request):
    # 添加公告
    print("******************")
    if request.method == "POST":
        json_str = request.body
        json_obj = json.loads(json_str)
        title = json_obj['title']
        content = json_obj['content']
        print(title)
        print(content)
        all_notices = Notice_list.objects.all()
        lists=[]
        for i in all_notices:
            uname=i.title
            lists.append(uname)
        if title in lists:
            return JsonResponse({"code": 301})
        Notice_list.objects.create(title=title, content=content)
        all_notice = Notice_list.objects.filter(title=title)
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
def notice_view(request):
    if request.method == "POST":
        # 当前公告内容显示
        json_str = request.body
        json_obj =json.loads(json_str)
        id=json_obj["id"]
        try:
            notice = Notice_list.objects.get(id=id)
            json2 = {}
            json2["title"] = notice.title
            json2["content"]=notice.content
            json2["updated_time"]=notice.updated_time
        except Exception as e:
            print(e)
            return JsonResponse({"code": 300, 'error': "显示失败"})
        return JsonResponse({"code": 200, "obj": json2})


@login_check
def notice_update_view(request,_id=None):
    # 修改公告
    if request.method == "GET":
        json2 = {}
        try:
            notice = Notice_list.objects.get(id=_id)
            json2["title"] = notice.title
            json2["content"] = notice.content
        except Exception as e:
            print(e)
        return JsonResponse({"code": 200, "obj":json2})
    elif request.method == "POST":
        json_str = request.body
        json_obj = json.loads(json_str)
        id = json_obj["id"]
        title=json_obj["title"]
        content=json_obj["content"]
        _title=json_obj["_title"]
        all_notices = Notice_list.objects.all()
        lists=[]
        for i in all_notices:
            if _title==i.title:
                continue
            else:
                lists.append(i.title)
        if title in lists:
            return JsonResponse({"code": 301})
        try:
            notice = Notice_list.objects.get(id=id)
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
def notice_delete_view(request):
    # 删除公告
    if request.method == "POST":
        json_str = request.body
        json_obj = json.loads(json_str)
        id = json_obj["id"]
        try:
            notice = Notice_list.objects.filter(id=id)
            notice.delete()
        except Exception as e:
            print(e)
            return JsonResponse({"code":300})
        return JsonResponse({"code": 200})
