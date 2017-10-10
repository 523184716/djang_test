#coding:utf-8

from  django import  forms
from .models import TestModleForm
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True,error_messages={"invalid":"邮箱格式错误"})

class ALogin(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    ipaddr = forms.GenericIPAddressField()

class Aloginmodelform(forms.ModelForm):

    class Meta:
        model = TestModleForm
        fields = "__all__"
