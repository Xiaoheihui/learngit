from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class test(APIView):
    def get(self, request, *args, **kwargs):
        return Response(['后台数据列表1', '后台列表数据2'])
