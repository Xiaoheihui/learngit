from django import forms
from django.core import validators
from . import models
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=10)
    email = forms.CharField(max_length=50)

    # 这个函数名字不能随便取，只能是  `clean_需要附件验证的字段名字`。
    def clean_username(self):
        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username=username).exists()
        if exists:
            # 验证失败抛出的异常
            raise forms.ValidationError(message='此用户名已经被注册')
        return username

    def get_errors(self):
        # 通过self.errors.get_json_data()获取错误的信息
        errors = self.errors.get_json_data()
        # 新建一个错误信息的字典，存储错误信息的字段和对应的错误信息
        new_errors = {}
        # 遍历获取的错误信息字典
        for key,message_dicts in errors.items():
            # 定义一个错误信息的列表，因为一个字段可能出现了多个错误，
            # 所以我们用一个列表将错误某个字段的所有错误信息存储起来
            messages = []
            # 遍历所有的错误信息，然后逐个添加至定义的messages列表中
            for message in message_dicts:
                message = message['message']
                messages.append(message)
            # 将获取的所有错误信息添加至自定义的字典中，并使用获取的key来对应
            new_errors[key] = messages
        # 返回自定义错误信息的字典
        return new_errors
