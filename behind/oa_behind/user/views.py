import random

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from tools.sms import YunTongXin
from django.utils.decorators import method_decorator

from user.models import UserProfile
import hashlib,jwt,time
from django.conf import settings
# Create your views here.
from django.views import View
from django.core.mail import send_mail
from tools.login_dec import login_check

#用户模块的错误码： 10100~10199

class UsersView(View):
    @method_decorator(login_check)
    def get(self,request,username=None):
        user = request.myuser
        data = {}
        # data['id'] = user.id
        data['username'] = user.username
        data['phone'] = user.phone
        data['email'] = user.email
        data['create_time'] = user.created_time
        result = {'code':200,'data':data}
        return JsonResponse(result)

    def put(self,request,username):
        json_str = request.body
        py_obj = json.loads(json_str)
        user = UserProfile.objects.get(username = username)
        try:
            user.phone = py_obj['phone']
            user.email = py_obj['email']
            user.save()
            result = {'code': 200}
        except:
            result = {'code': 10103, 'error': "数据修改错误！"}
        return JsonResponse(result)

    def post(self,request):
        json_str = request.body
        py_obj = json.loads(json_str)
        username = py_obj['username']
        email = py_obj['email']
        phone = py_obj['phone']
        password_1 = py_obj['password_1']
        password_2 = py_obj['password_2']
        isActive = py_obj['isActive']
        is_induction = py_obj['is_induction']
        vericode = py_obj['vericode']
        print(username,phone,email)
        cache_key = 'sms_%s' % phone
        smsCode = cache.get(cache_key)

        if not smsCode:
            result = {'code': 10106, 'error': '验证码已过期！'}
            return JsonResponse(result)
        else:
            if vericode != str(smsCode):
                result = {'code': 10105, 'error': '验证码错误！'}
                return JsonResponse(result)

        if len(username)>20:
            result = {'code':10100,'error':'用户名长度不能超过20个字符串！'}
            return JsonResponse(result)
        # print('****************')
        if password_1 != password_2:
            result = {'code': 10101, 'error': '两次密码输入要一致！'}
            return JsonResponse(result)
        old_user = UserProfile.objects.filter(username = username)
        if old_user:
            result = {'code': 10102, 'error': '用户名已存在！'}
            return JsonResponse(result)

        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_h= md5.hexdigest()

        try:
            user = UserProfile.objects.create(username=username,password=password_h,
                                              email=email,
                                              phone = phone,
                                              nickname=username,
                                              isActive=isActive,
                                              is_induction=is_induction,
                                              )
        except:
            result = {'code': 10103, 'error': '用户名已存在！'}
            return JsonResponse(result)
        token = make_token(username)

        return JsonResponse({'code':200,'username':username,'data':{'token':token.decode()}})

def make_token(username,expire = 3600*24):
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username':username,'exp':now+expire}
    return jwt.encode(payload,key,algorithm='HS256')

def sendEmail(request):
    json_str = request.body
    py_obj = json.loads(json_str)
    username = py_obj['username']
    email = py_obj['email']
    print(username)
    print(email)

    user = UserProfile.objects.get(username=username)
    print(user.username)
    print(email)
    print(user.email)
    if email == user.email:
        veriCode = random.randint(1000,9999)
        send_mail('验证码', f'用户验证码为：{veriCode}', '941582519@qq.com',
                  (email,),fail_silently=False)
        result = {'code':'200','veriCode': veriCode}
    else:
        print()
        result = {'code':'30333','error':'您使用的不是注册邮箱！'}
        print('您使用的不是注册邮箱！')
    return JsonResponse(result)
def sendSms(request):
    json_str = request.body
    py_obj = json.loads(json_str)
    phone = py_obj['phone']
    code = random.randint(1000, 9999)
    print(phone, code)
    cache_key = 'sms_%s' % phone
    cache.set(cache_key, code, 200)

    x = YunTongXin(settings.SMS_ACCOUNT_ID,
                   settings.SMS_ACCOUNT_TOKEN,
                   settings.SMS_APP_ID,
                   settings.SMS_TEMPLATE_ID)
    res = x.run(phone, code)
    print(res)
    return JsonResponse({'code': 200})

@login_check
def passwordChange(request,username):

    json_str = request.body
    py_obj = json.loads(json_str)
    oldPassword = py_obj['oldPassword']
    newPassword = py_obj['newPassword']
    user = UserProfile.objects.get(username=username)
    md5 = hashlib.md5()
    md5.update(oldPassword.encode())
    password_h = md5.hexdigest()


    if password_h == user.password:
        md5 = hashlib.md5()
        md5.update(newPassword.encode())
        password_k = md5.hexdigest()
        user.password = password_k
        user.save()
        return JsonResponse({'code':200})
    else:
        return JsonResponse({'code':20100,'error':'密码错误！'})


def passwordGet(request,username):
    print('YYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
    json_str = request.body
    py_obj = json.loads(json_str)
    password = py_obj['password']
    user = UserProfile.objects.get(username=username)
    md5 = hashlib.md5()
    md5.update(password.encode())
    password_h = md5.hexdigest()

    try:
        user.password = password_h
        user.save()
        result = {'code': 200}
    except:
        result = {'code': 10103, 'error': "密码修改错误！"}
    return JsonResponse(result)


# @login_check
# def changeInfo(request,username):
#     json_str = request.body
#     py_obj = json.loads(json_str)
#     user = UserProfile.objects.get(username=username)
#     try:
#         user.phone = py_obj['phone']
#         user.email = py_obj['email']
#         user.save()
#         result = {'code': 200}
#     except:
#         result = {'code': 10103, 'error': "数据修改错误！"}
#     return JsonResponse(result)


