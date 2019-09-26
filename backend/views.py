from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Q, F
from django.contrib.auth.models import User
from .forms import RegisterForm, MessageForm
import json
from django.contrib import auth
from django.db import models
from django.forms.models import model_to_dict
from .models import CompInfo, CompClass, CompLevel, Area

import datetime,pytz

tz = pytz.timezone('Asia/Shanghai')


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
    user_name = auth.authenticate(username=user, password=pwd)  # 自动校验user表 用户账号校验
    try:
        userEmail = User.objects.get(email=user)
    except:
        userEmail = None

    if user_name is not None:  # 登陆成功
        response1 = Model_To_Dict(user_name)
        response2 = Model_To_Dict(user_name.usermessage)
        response = {**response1, **response2}
        user_name.last_login = datetime.datetime.now() + datetime.timedelta(hours=8)
        user_name.save()
        response["status"] = 0
    elif userEmail is not None:
        user_email = auth.authenticate(username=userEmail, password=pwd)  # 自动校验user表 用户邮箱校验
        if user_email is not None:
            response1 = Model_To_Dict(user_email)
            response2 = Model_To_Dict(user_email.usermessage)
            response = {**response1, **response2}
            user_email.last_login = datetime.datetime.now() + datetime.timedelta(hours=8)
            user_email.save()
            response["status"] = 0
        else:
            response["status"] = 1
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
        if response['UBirthday'] is not None:
            response["UBirthday"] = response["UBirthday"].strftime("%Y-%m-%d")
        else:
            response['UBirthday'] = 0
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
        dateTime = datetime.datetime.strptime(dateStr, '%Y-%m-%d') + datetime.timedelta(hours=24)
        print(dateTime)
        # 修改POST内容
        data = request.POST.copy()
        data['birthday'] = dateTime
        form = MessageForm(data)
        if form.is_valid():
            user.usermessage.UBirthday = form.cleaned_data.get('birthday')
            user.usermessage.Unickname = form.cleaned_data.get('nickname')
            user.usermessage.USex = form.cleaned_data.get('sex')
            user.usermessage.UStatement = form.cleaned_data.get('statement')
            user.save()
            print(model_to_dict(user.usermessage))
            response["status"] = 0
        else:
            if 'nickname' in form.errors.keys():
                response["message"] = form.errors["nickname"][0]
            elif 'statement' in form.errors.keys():
                response["message"] = form.errors["statement"][0]
            else:
                print(form.errors)
                response["message"] = "信息修改失败！未知错误。"
                response["status"] = 1
    else:
        response["status"] = 1

    return JsonResponse(response)


# 获取比赛信息
@require_http_methods(["POST"])
def getCompInfoByClassId(request):
    response = {}
    comp = []
    classId = int(request.POST.get("classId"))
    compInfo = CompInfo.objects.filter(IClass_id=classId)
    if compInfo is not None:
        for info in compInfo:
            comp.append(Model_To_Dict(info))
        response['compInfo'] = comp
        response['status'] = 0
        response['messsage'] = '比赛信息返回成功'
    else:
        response['status'] = 1
        response['message'] = '比赛信息返回失败，请重试！'
    return JsonResponse(response)


# 根据比赛信息id获得单条比赛信息
@require_http_methods(["POST"])
def getCompInfoByCompId(request):
    response = {}
    compId = int(request.POST.get('compId'))
    compInfo = CompInfo.objects.get(Iid=compId)
    if compInfo is not None:
        response = model_to_dict(compInfo)
        compLevelinfo = CompLevel.objects.get(ID=response['ILevel'])
        compLevel = Model_To_Dict(compLevelinfo)['Name']
        compClassinfo = CompClass.objects.get(Cid=response['IClass'])
        compClass = Model_To_Dict(compClassinfo)['CName']
        compAreainfo = Area.objects.get(ID=response['IAreaID'])
        compArea = Model_To_Dict(compAreainfo)['Name']
        response['status'] = 0
        response['compLevel'] = compLevel
        response['compClass'] = compClass
        response['compArea'] = compArea
    else:
        response['status'] = 1
        response['message'] = '该比赛信息不存在，请重试！'
    return JsonResponse(response)


# 根据筛选信息获取比赛信息
@require_http_methods(["POST"])
def getCompInfoBySelect(request):
    response = {}
    comp = []
    gamelevel = int(request.POST.get('gameLevel'))
    gameClass = int(request.POST.get('gameClass'))
    selectStart = request.POST.get('selectStart')
    selectEnd = request.POST.get('selectEnd')
    if selectStart == '':
        startTime = datetime.datetime.strptime('1900-01-01', '%Y-%m-%d')
    else:
        dateStr = selectStart[:10]  # 截取时间字符串
        startTime = datetime.datetime.strptime(dateStr, '%Y-%m-%d') + datetime.timedelta(hours=24)
    if selectEnd == '':
        endTime = datetime.datetime.strptime('2100-01-01', '%Y-%m-%d')
    else:
        dateStr = selectEnd[:10]  # 截取时间字符串
        endTime = datetime.datetime.strptime(dateStr, '%Y-%m-%d') + datetime.timedelta(hours=24)
    print(startTime,endTime)
    if gamelevel == 0:
        compinfos = CompInfo.objects.filter(IClass=gameClass, IApplyStartTime__gte=startTime, IApplyEndTime__lte=endTime)
    else:
        compinfos = CompInfo.objects.filter(IClass=gameClass, ILevel=gamelevel, IApplyStartTime__gte=startTime, IApplyEndTime__lte=endTime)
    if compinfos is not None:
        for item in compinfos:
            comp.append(Model_To_Dict(item))
        response['compInfo'] = comp
        response['status'] = 0
        response['message'] = '筛选成功!'
    else:
        response['status'] = 1
        response['message'] = '信息筛选失败，请重试！'
    return JsonResponse(response)


# 辅助函数：
def Model_To_Dict(model, fields=None, exclude=None):
    dic = model_to_dict(model, fields, exclude)
    for key in dic:
        if isinstance(dic[key], datetime.datetime):
           dic[key] = dic[key].strftime("%Y-%m-%d %H:%M")

    return dic