import json

from django.http import JsonResponse

from department.models import Department, Position
from management.models import Management
from user.models import UserProfile


def add_management(request):
    if request.method == "POST":
        js_str = request.body
        py_obj = json.loads(js_str)
        name = py_obj['name']
        sex = py_obj["sex"]
        job_no = py_obj['job_no']
        dep_name = py_obj['dep_name']
        position = py_obj['position_name']
        img = py_obj['img']
        power = py_obj['power']
        username = py_obj['username']
        email = py_obj['email']
        phone = py_obj['phone']

        if not name or  not job_no or not dep_name or not position:
            result = {"code":10401,"error":"请填写内容"}
            return JsonResponse(result)
        old_job_no = Management.objects.filter(job_no=job_no)
        if old_job_no:
            result = {"code":10402,"error":"请重新输入工号"}
            return JsonResponse(result)
        try:
            department1 = Department.objects.get(name=dep_name)
        except:
            department1=Department.objects.create(name=dep_name)

        # print(department1)
        try:
            position1 = Position.objects.get(name=position)
        except:
            position1=Position.objects.create(name=position,
                                    dep_name=dep_name,
                                    description='',
                                    department=department1)
        try:
            user1 = UserProfile.objects.get(username=username)
        except:
            user1=UserProfile.objects.create(
                username=username,
                nickname=name,
                email=email,
            )

        Management.objects.create(
            job_no=job_no,
            dep_name=dep_name,
            position_name=position,
            sex = sex,
            name = name,
            img = img,
            power = power,
            username = username,
            email = email,
            phone = phone,
            department=department1,
            position=position1,
            user=user1
        )

        result = {"code":200}
        return JsonResponse(result)

    result = {"code":10400,"error":"Give me Post!"}
    return JsonResponse(result)


def management_list(request):
    if request.method == 'GET':
        management_all = Management.objects.all()
        if not management_all :
            result = {'code': 10300, 'error': '没有信息'}
            return JsonResponse(result)
        else:
            obj = {}
            # obj={'':{},'':{}}
            # for department in department_all:
            for management in management_all:
                obj[management.id] = {
                    "id": management.id,
                    "dep_name": management.dep_name,
                    "username": management.username,
                    "name": management.name,
                    "position_name": management.position_name,
                    "job_no": management.job_no,
                    "sex": management.sex,
                    "power": management.power,
                }

            return JsonResponse({"code": 200, "data": obj})


def search_management(request):
    if request.method == "POST":
        print(11111111)
        js_str = request.body
        py_obj = json.loads(js_str)
        print(py_obj)
        name = py_obj['name']
        job_no = py_obj['job_no']

        if not name or not job_no:
            result = {'code': 10411, 'error': '请输入信息'}
            return JsonResponse(result)

        management1 = Management.objects.filter(name=name,
                                                 job_no=job_no)
        print(management1)
        if  not management1 :
            result = {'code': 10411, 'error': '请重新输入信息'}
            return JsonResponse(result)

        obj = {}
        # obj={'':{},'':{}}
        for management in management1:

            obj[management.id] = {
                "id": management.id,
                "dep_name": management.dep_name,
                "username": management.username,
                "name": management.name,
                "position_name": management.position_name,
                "job_no": management.job_no,
                "sex": management.sex,
                "power": management.power,
                }

        return JsonResponse({"code": 200, "data": obj})

    result = {'code': 10412, 'error': '给我post'}
    return JsonResponse(result)






