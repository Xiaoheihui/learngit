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
from .models import CompInfo, CompClass, CompLevel, Area, UserMessage, BBSSection, BBSTopic, \
    BBSReply, MarkMessage, CompRecord

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

# 注册
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
        user.usermessage.Unickname = username # 默认昵称
        user.save()
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
        # 具体赛事信息
        response = model_to_dict(compInfo)
        compLevelinfo = CompLevel.objects.get(ID=response['ILevel'])
        compLevel = Model_To_Dict(compLevelinfo)['Name']
        compClassinfo = CompClass.objects.get(Cid=response['IClass'])
        compClass = Model_To_Dict(compClassinfo)['CName']
        compAreainfo = Area.objects.get(ID=response['IAreaID'])
        compArea = Model_To_Dict(compAreainfo)['Name']
        # 赛事记录
        promulgatorID = int(compInfo.comprecord.RPromulgatorID.id)
        response['promulgator'] = User.objects.get(id=promulgatorID).usermessage.Unickname # 昵称
        response['statement'] = compInfo.comprecord.RStatement
        response['time'] = compInfo.comprecord.RTime.strftime("%Y-%m-%d %H:%M")
        # 点击数+1
        compInfo.comprecord.RClickCount += 1
        compInfo.comprecord.save()
        response['chickCount'] = compInfo.comprecord.RClickCount
        response['markCount'] = compInfo.comprecord.RMarkCount
        response['Rid'] = compInfo.comprecord.RID # 记录id



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
    gamearea = int(request.POST.get('gameArea'))
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
    print(startTime, endTime)
    if gamelevel == 0:
        if gamearea == 0:
            compinfos = CompInfo.objects.filter(IClass=gameClass, IApplyStartTime__gte=startTime, IApplyEndTime__lte=endTime)
        elif gamearea == 100:
            compinfos = CompInfo.objects.filter(IClass=gameClass, IApplyStartTime__gte=startTime, IApplyEndTime__lte=endTime).exclude(IAreaID=1).exclude(IAreaID=2).exclude(IAreaID=20).exclude(IAreaID=36)
        else:
            compinfos = CompInfo.objects.filter(IClass=gameClass, IApplyStartTime__gte=startTime, IApplyEndTime__lte=endTime, IAreaID=gamearea)
    else:
        if gamearea == 0:
            compinfos = CompInfo.objects.filter(IClass=gameClass, ILevel=gamelevel, IApplyStartTime__gte=startTime, IApplyEndTime__lte=endTime)
        elif gamearea == 100:
            compinfos = CompInfo.objects.filter(IClass=gameClass, ILevel=gamelevel, IApplyStartTime__gte=startTime, IApplyEndTime__lte=endTime).exclude(IAreaID=1).exclude(IAreaID=2).exclude(IAreaID=20).exclude(IAreaID=36)
        else:
            compinfos = CompInfo.objects.filter(IClass=gameClass, ILevel=gamelevel, IApplyStartTime__gte=startTime, IApplyEndTime__lte=endTime, IAreaID=gamearea)
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

# 用户发送帖子
@require_http_methods(["POST"])
def sendBBS(request):
    response = {}
    userid = int(request.POST.get('userId'))
    bbsClass = int(request.POST.get('bbsClass'))
    bbsName = request.POST.get('bbsName')
    bbsContent = request.POST.get('bbsContent')
    sendTime = datetime.datetime.now()
    user = UserMessage.objects.get(id=userid)
    bbssection = BBSSection.objects.get(Sid=bbsClass)
    bbsinfo = {
        'TTopic':bbsName,
        'TContents':bbsContent,
        'TUid':user,
        'TSid':bbssection,
        'TLastClickT':sendTime
    }
    try:
        BBSTopic.objects.create(**bbsinfo)
        response['status'] = 0
        response['message'] = '发送成功!'
    except:
        response['status'] = 1
        response['message'] = '发送失败，请重试!'
    return JsonResponse(response)

# 根据板块ID获取帖子信息
@require_http_methods(["POST"])
def getBBSByClassId(request):
    response = {}
    bbsinfos = []
    bbsId = int(request.POST.get('bbsId'))
    try:
        bbslist = BBSTopic.objects.filter(TSid=bbsId)
        for bbs in bbslist:
            bbsinfo = Model_To_Dict(bbs)
            userinfo = Model_To_Dict(UserMessage.objects.get(id=bbsinfo['TUid']))
            bbsinfo['userName'] = userinfo
            bbsinfos.append(dict(bbsinfo, **userinfo))
        response['bbsinfo'] = bbsinfos
        response['status'] = 0
        response['message'] = '帖子信息返回成功！'
    except:
        response['status'] = 1
        response['message'] = '帖子信息返回失败，请重试！'
    return JsonResponse(response)

# 根据用户ID获取帖子信息
@require_http_methods(["POST"])
def getBBSByUserId(request):
    response = {}
    bbsinfos = []
    userId = int(request.POST.get('userId'))
    try:
        bbslist = BBSTopic.objects.filter(TUid=userId)
        for bbs in bbslist:
            bbsinfo = Model_To_Dict(bbs)
            userinfo = Model_To_Dict(UserMessage.objects.get(id=bbsinfo['TUid']))
            bbsClass = Model_To_Dict(BBSSection.objects.get(Sid=bbsinfo['TSid']))['SName']
            bbsinfo['userName'] = userinfo
            bbsinfo['bbsClass'] = bbsClass
            bbsinfos.append(dict(bbsinfo, **userinfo))
        response['bbsinfo'] = bbsinfos
        response['status'] = 0
        response['message'] = '帖子信息返回成功！'
    except:
        response['status'] = 1
        response['message'] = '帖子信息返回失败，请重试！'
    return JsonResponse(response)

# 根据帖子ID来删除帖子
@require_http_methods(["POST"])
def deleteBBS(request):
    response = {}
    bbsId = request.POST.get('bbsId')
    try:
        BBSTopic.objects.get(Tid=bbsId).delete()
        BBSReply.objects.filter(RTid=bbsId).delete()
        response['status'] = 0
        response['message'] = '帖子删除成功！'
    except:
        response['status'] = 1
        response['message'] = '帖子删除失败，请重试！'
    return JsonResponse(response)


@require_http_methods(["POST"])
def markComp(request):
    response = {}
    compId = int(request.POST.get('compId'))
    userId = int(request.POST.get('userId'))
    try:
        compRecord = CompRecord.objects.get(RID=compId)
        user = User.objects.get(pk=userId).usermessage
        # 判断传入用户、帖子数据是否存在数据库中
        try:
            ifMark = MarkMessage.objects.get(CompRecordId=compRecord, UsersId=user)
            response['status'] = 2
            response['message'] = '您已收藏过该条记录，请勿重复操作。'
        except:
                MarkMessage.objects.create(CompRecordId=compRecord, UsersId=user)
                response['status'] = 0
                response['message'] = '收藏成功！'
        #     else:
        #
        # else:
        #     response['status'] = 1
        #     response['message'] = '收藏失败，赛事记录可能已被删除，请刷新后重试！'
    except:
        response['status'] = 1
        response['message'] = '收藏失败，请稍后重试！'
    return JsonResponse(response)


@require_http_methods(["POST"])
def DeleteMarkMessage(request):
    response = {}
    compId = int(request.POST.get('compId'))
    userId = int(request.POST.get('userId'))
    try:
        compRecord = CompInfo.objects.get(Iid=compId).comprecord
        user = User.objects.get(pk=userId).usermessage
        MarkMessage.objects.get(CompRecordId=compRecord, UsersId=user).delete()
        response['status'] = 0
        response['message'] = '成功取消收藏！'
    except:
        response['status'] = 1
        response['message'] = '取消收藏失败，请刷新后重试！'
    return JsonResponse(response)

@require_http_methods(["POST"])
def getMarkMessage(request):
    response = {}
    userId = int(request.POST.get('userId'))
    try:
        user = User.objects.get(pk=userId).usermessage
        marklist = MarkMessage.objects.filter(UsersId=user)
        markMessages = []
        for message in marklist:
            compInfoId = message.CompRecordId.RContentID.Iid
            compTitle  = message.CompRecordId.RTitle
            markMessages.append(
                {"compInfoId": compInfoId,
                 "compTitle" : compTitle },
            )
        response['markMessages'] = markMessages
        response['markMessagesCount'] = len(markMessages)
        response['status'] = 0
        response['message'] = '查询成功'
    except:
        response['status'] = 1
        response['message'] = '查询失败，请稍后重试！'
    return JsonResponse(response)




# 辅助函数：
def Model_To_Dict(model, fields=None, exclude=None):
    dic = model_to_dict(model, fields, exclude)
    print(dic)
    for key in dic:
        if isinstance(dic[key], datetime.datetime):
           dic[key] = dic[key].strftime("%Y-%m-%d %H:%M")

    return dic