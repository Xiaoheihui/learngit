from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import RegisterForm
import json
from django.contrib import auth
from django.forms.models import model_to_dict

import datetime, re

# Create your views here.
# from rest_framework.views import APIView
# from rest_framework.response import Response


# class test(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response(['后台数据列表1', '后台列表数据2'])
def index(request):
    request.META["CSRF_COOKIE_USED"] = True
    return render(request, 'index.html')

@require_http_methods(["POST"])
def test(request):
    response = {}
    birthday = request.POST.get('birthday')
    print(type(birthday))
    print(birthday)
    return JsonResponse(response)

@require_http_methods(["POST"])
def register(request):
    response = {}
    form = RegisterForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        User.objects.create_user(username=username, email=email, password=password)

        response["message"] = 'success'
        response["status"] = 0
        response["content"] = ['1', '2']
        user = User.objects.get(username=username)
        print(Model_To_Dict(user.usermessage, fields=["Unickname", "UBirthday", "USex", "UStatement"]))

    else:
        if 'email' in form.get_errors().keys():
            response["message"] = form.errors["email"][0]
        elif 'username' in form.get_errors().keys():
            response["message"] = form.errors["username"][0]
        else:
            response["message"] = "注册失败！未知错误。"
        response["status"] = 1


    return JsonResponse(response)

# 登录函数
@require_http_methods(["POST"])
def login(request):
    response = {}
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    user = auth.authenticate(username=user, password=pwd)  # 自动校验user表
    if user is not None:  # 登陆成功
        response1 = Model_To_Dict(user)
        response2 = Model_To_Dict(user.usermessage)
        response = response1.update(response2)
        response["status"] = 0
    else:
        response["status"] = 1

    return JsonResponse(response)


# 获取用户信息
@require_http_methods(["POST"])
def getMessage(request):
    response = {}
    id = request.POST.get("id")
    user = User.objects.get(pk=id)
    if user is not None:  # 查询成功
        response = Model_To_Dict(user.usermessage, fields=["Unickname", "UBirthday", "USex", "UStatement"])
        response["UBirthday"] = response["UBirthday"].spilt(" ")[0] # 时间格式
        response["status"] = 0
    else:
        response["status"] = 1

    return JsonResponse(response)


# 修改用户信息
@require_http_methods(["POST"])
def alterMessage(request):
    response = {}
    id = request.POST.get("id")
    user = User.objects.get(pk=id)
    if user is not None:  # 查询成功
        dateStr = request.POST.get("birthday")[:10]# 截取时间字符串
        dateTime = datetime.datetime.strptime(dateStr, '%Y-%m-%d')
        # 修改POST内容
        data = request.POST.copy()
        data['birthday'] = dateTime

        form = RegisterForm(request.POST)
        if form.is_valid():
            user.usermessage.UBirthday = form.cleaned_data.get('birthday')
            user.usermessage.Unickname = form.cleaned_data.get('nickname')
            user.usermessage.USex = form.cleaned_data.get('sex')
            user.usermessage.UStatement = form.cleaned_data.get('statement')
            response["status"] = 0
        else:
            if 'nickname' in form.errors.keys():
                response["message"] = form.errors["nickname"][0]
            elif 'statement' in form.errors().keys():
                response["message"] = form.errors["statement"][0]
            else:
                response["message"] = "信息修改失败！未知错误。"
                response["status"] = 1
    else:
        response["status"] = 1

    return JsonResponse(response)


# 辅助函数：
def Model_To_Dict(model, fields=None, exclude=None):
    dic = model_to_dict(model, fields, exclude)
    for key in dic:
        if isinstance(dic[key], datetime.datetime):
           dic[key] = dic[key].strftime("%Y-%m-%d %H:%M")

    return dic