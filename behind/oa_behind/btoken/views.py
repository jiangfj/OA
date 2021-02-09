import json,hashlib
from user.views import make_token
from django.http import JsonResponse
from user.models import UserProfile
# Create your views here.
from django.views import View


#异常码  10200-10299
class Token_View(View):
    def post(self,request):
        json_str = request.body
        py_obj = json.loads(json_str)
        username = py_obj['username']
        password = py_obj['password']
        print(username,password)

        try:
            user=UserProfile.objects.get(username=username)
        except:
            result = {'code':10200,'error':'用户名或密码错误！'}
            return JsonResponse(result)


        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h != user.password:
            result = {'code':10201,'error':'用户名或密码错误！'}
            return JsonResponse(result)
        token = make_token(username)

        return JsonResponse({'code':200,'username':username,'data':{'token':token.decode()}})