from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
import requests
from lxml import etree


def get_weather(request):
    if request.method == 'POST':
        json_str = request.body
        json_obj = json.loads(json_str)
        city = json_obj['city']
        print(city)

        if not city:
            result = {"code": 10501, "error": "请填写城市！"}
            return JsonResponse(result)

        url = 'https://www.tianqi.com/tianqi/search?keyword=' + city
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        response = requests.get(url=url,headers=headers)
        tree = etree.HTML(response.text)
        # 检测城市天气是否存在
        try:
            city = tree.xpath('//dd[@class="name"]/h2/text()')[0]
        except:
            content = '没有该城市天气信息，请确认查询格式'
            result = {'code':10502,'error':content}
            return JsonResponse(result)
        week = tree.xpath('//dd[@class="week"]/text()')[0]
        now = tree.xpath('//p[@class="now"]')[0].xpath('string(.)')
        temp = tree.xpath('//dd[@class="weather"]/span')[0].xpath('string(.)')
        shidu = tree.xpath('//dd[@class="shidu"]/b/text()')
        kongqi = tree.xpath('//dd[@class="kongqi"]/h5/text()')[0]
        pm = tree.xpath('//dd[@class="kongqi"]/h6/text()')[0]
        # content = "【{0}】{1}天气\n当前温度：{2}\n今日天气：{3}\n{4}\n{5}\n{6}".format(city, week.split('\u3000')[0], now, temp, '\n'.join(shidu),kongqi,pm)
        result = {"code":200,
                  'content':{
            'title':'【{}】{}天气'.format(city, week.split('\u3000')[0]),
            '当前温度':'{}'.format(now),
            '今日天气':'{}'.format(temp),
            '湿度':'{}'.format('\n'.join(shidu)),
            '风向':'{}'.format(kongqi),
            'PM':'{}'.format(pm)
                  }
        }
        return JsonResponse(result)
    else:
        result = {'code': 10503, "error": "Give me POST!"}
        return JsonResponse(result)