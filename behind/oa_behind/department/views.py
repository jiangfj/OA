import json
import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from department.models import Department, Position
from management.models import Management


def department(request):
    # js_str = request.body
    # py_obj = json.loads(js_str)
    # department = py_obj['department']
    # id = py_obj['id']
    # position = py_obj['position']
    # info = py_obj['info']

    if request.method == 'GET':
        department_all = Department.objects.all()
        position_all = Position.objects.all()

        if not department_all and not position_all:
            result = {'code': 10300, 'error': '没有信息'}
            return JsonResponse(result)
        else:
            obj = {}
            # obj={'':{},'':{}}
            # for department in department_all:
            for position in position_all:
                obj[position.id] = {
                    "id": position.id,
                    "dep_name": position.dep_name,
                    "position_name": position.name,
                    "description":position.description

                }

            return JsonResponse({"code": 200, "data": obj})



def add_department(request):
    if request.method == 'POST':
        js_str = request.body

        py_obj = json.loads(js_str)
        print(py_obj)
        department = py_obj['department']
        if not department:
            result = {'code':10310,'error':'请输入内容'}
            return JsonResponse(result)
        # print(department)
        old_department = Department.objects.filter(name = department)
        if old_department:
            result = {'code':10313,'error':'部门已存在!'}
            return JsonResponse(result)



        Department.objects.create(name = department)

        try:
            department1 = Department.objects.get(name=department)

        except:
            result = {'code': 10312, 'error': '服务器忙'}
            return JsonResponse(result)
        Position.objects.create(name = '',
                                    dep_name = department,
                                    description = '',
                                    department=department1)

        result = {'code': 200}
        return JsonResponse(result)

    else:
        result = {'code': 10311, 'error': '给我 POST 请求!'}
        return JsonResponse(result)

def add_position(request):
    if request.method == 'POST':
        js_str = request.body
        py_obj = json.loads(js_str)
        # print(py_obj)
        dep_name = py_obj['dep_name']
        position = py_obj['position']
        description = py_obj['description']
        if not dep_name or not position:
            result = {'code': 10321, 'error': '请输入内容'}
            return JsonResponse(result)


        obj = Department.objects.filter(name=dep_name)
        if not obj:
            Department.objects.create(name=dep_name)
        department1 = Department.objects.get(name=dep_name)
        # print(department1)
        Position.objects.create(name=position,
                            dep_name=dep_name,
                            description=description,
                            department=department1)

        result = {'code': 200}
        return JsonResponse(result)


    else:
        result = {'code': 10327, 'error': '我是 POST 请求!'}
        return JsonResponse(result)


#
# def del_department(request):
#     if request.method == "DELETE":
#         js_str = request.body
#         py_obj = json.loads(js_str)
#         department = py_obj['department']
#
#
#
#
#         print(department)
#         if not department:
#             print(11111)
#             result = {'code': 10331, 'error': '选择要删除的部门'}
#             return JsonResponse(result)
#         department1 = Department.objects.filter(name=department)
#         if not department1:
#             result = {'code': 10332, 'error': '没有该部门'}
#             return JsonResponse(result)
#
#         try:
#             management = Management.objects.get(department=department)
#             if department in getattr(management,'department'):
#                 result = {'code': 10333, 'error': '请先删除该部门员工'}
#                 return JsonResponse(result)
#         except:
#             result = {'code': 10333, 'error': '请重新选择'}
#             return JsonResponse(result)
#
#
#         position = Position.objects.filter(dep_name=department)
#         if department in getattr(position,'dep_name'):
#             result = {'code': 10333, 'error': '请先删除该部门职位'}
#             return JsonResponse(result)
#
#         department1.delete()
#         result = {'code':200}
#         return JsonResponse(result)
#
#     else:
#         result = {'code': 10327, 'error': '我是 DELETE 请求!'}
#         return JsonResponse(result)

