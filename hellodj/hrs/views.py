from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template
from random import randrange

# Create your views here.

def home(request):
    fruits = ['西瓜','香蕉','蜜桃','龙眼','草莓']
    start,end = 0,randrange(len(fruits))
    fruits = fruits[start:end+1]
    ctx = {
        'greeting':'你好',
        'current_time':datetime.now(),
        'fruits':fruits
    }
    # 第二个参数是模板页面，在setting.py里进行配置
    # 第三个参数是一个字典（保存替换模板占位符的数据）
    return render(request,'index.html',ctx)