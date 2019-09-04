from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import RegisterForm
import json

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
    form = RegisterForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        User.objects.create_user(name=username, email=email, password=password)

        response["msg"] = 'success'
        response["status"] = 0
        response["content"] = ['1', '2']

    else:
        response["msg"] = "注册失败"
        response["status"] = 1

    return JsonResponse(response)

