from django.http import JsonResponse
from management.models import Management
import json

def address_book_list(request):
    """通讯录模块"""

    #取值，部门和查询内容
    js_str=request.body
    py_obj=json.loads(js_str)
    department=py_obj['department']
    query=py_obj['query']
    print(department,query)

    if not department:
        #部门为空，部门一定不能为空
        if not query:
            #查询内容为空
            result = {'code': 10100, 'error': '请输入查询信息！'}
            return JsonResponse(result)
        else:
            # 查询内容不为空
            result = {'code': 10101, 'error': '请选择部门！'}
            return JsonResponse(result)
    else:
        #部门不为空
        if not query:
            #查询内容为空
            result={'code':10102,'error':'请输入姓名或电话！'}
            return JsonResponse(result)
        else:
            # 查询内容不为空
            if len(query) == 11:
                # 查询内容为手机号，一般只有一条
                try:
                    user_all = Management.objects.get(phone=query)
                except:
                    result = {'code': 10103, 'error': '没有此手机号的小主！'}
                    return JsonResponse(result)

                result = {'code': 200, 'data': {}}
                result['data']['id'] = user_all.id
                result['data']['name'] = user_all.name
                result['data']['sex'] = user_all.sex
                result['data']['dep_name'] = user_all.dep_name
                result['data']['position_name'] = user_all.position_name
                result['data']['phone'] = user_all.phone
                result['data']['email'] = user_all.email
                result['data']['create_time'] = user_all.create_time
                result['data']['job_no'] = user_all.job_no

                return JsonResponse(result)
            else:
                # 查询内容为姓名，有可能有多条
                all_user = Management.objects.filter(dep_name=department,name=query)
                print(all_user)
                if not all_user:
                    result = {'code': 10104, 'error': '查无此人！请重新输入！'}
                    return JsonResponse(result)
                else:
                    obj = {}
                    # obj={{'id':{'id','name'}},{'id':{'id','name'}}}
                    for user in all_user:
                        obj[user.id]={
                                "id": user.id,
                                "uname":user.name,
                                "sex":user.sex,
                                "dep_name":user.dep_name,
                                "position_name":user.position_name,
                                "phone":user.phone,
                                "email":user.email,
                                "create_time":user.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                                "job_no":user.job_no,

                            }

                        return JsonResponse({"code":200,"data":obj})
