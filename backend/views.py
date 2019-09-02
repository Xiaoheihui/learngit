from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
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
    try:
        response["msg"] = 'success'
        response["status"] = 200
        response["content"] = ['1', '2']
    except Exception as e:
        response["msg"] = str(e)
        response["status"] = 404
    return JsonResponse(response)

