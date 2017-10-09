# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from  django.http import  HttpResponse
from  .forms import  RegisterForm
from .models import  Asset,Userinfo,UserName,GroupName
def List(request,id,name):
    print  name,id
    return  HttpResponse('login')
# Create your views here.

def Add(request,name):
    Asset.objects.create(hostname=name)

    return HttpResponse('ok')

def Delete(request,id):
    Asset.objects.get(id=id).delete()
    return  HttpResponse('ok')

def Update(reuqest,id,hostname):
    #单一数据的添加
    """
    obj = Asset.objects.get(id=id)
    obj.hostname = hostname
    obj.save()
    """
    #批量匹配添加
    Asset.objects.filter(id__gt=id).update(hostname=hostname)
    return HttpResponse('ok')

def Query(request,hostname):
    """
    print 222
    query_list = Asset.objects.filter(hostname__contains=hostname)  ##这个字段包含这个字符串的查询
    print type(query_list)
    for i in query_list:
        print i.id
    """
    #取所有数据中的前两个
    ##id__in=（1,2,3）匹配在这个里面的输出
    allData = Asset.objects.all()
    #tmepData = Asset.objects.all().order_by('-id')  ###倒序
    for i in allData[0:2]:
        print i.id
    perData = Asset.objects.all().values('id','hostname')  #取指定字段的值
    print perData

    return  HttpResponse('ok')

def AseetList(request):
    assetlist = Asset.objects.all()
    return  render_to_response('assetlist.html',{'data':assetlist,'user':'alex'})

def Login(request):
    ret = {"status":""}
    if request.method == "POST":
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        is_empty = all([user,pwd])
        if is_empty:
            result = Userinfo.objects.filter(username=str(user),password=str(pwd)).count()
            print user,pwd
            if result==1:
                #return  AseetList(request)
                #return  render_to_response('index.html')
                return  redirect('/webapp/index/')
            else:
                return  render_to_response('login.html',{"status":"用户和密码错误"})
                #ret["status"] = "用户和密码错误"
        else:
            return  render_to_response('login.html',{"status":"用户名和密码不能为空"})
           # ret["status"] = "用户名和密码不能为空"
        #print ret["status"]
        #return render_to_response('login.html',{"status":ret["status"]}）

    else:
        return render_to_response('login.html')

def Register(request):
    registerForm = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        else:
            temp = form.errors.as_data()
            print temp["email"][0][0]

    return  render_to_response('register.html',{'form':registerForm})
    """
    if request.method == "POST":
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        result = Userinfo.objects.filter(username=str(user),password=str(pwd)).count()
        print user,pwd
        if result==1:
            return  AseetList(request)
        else:
            return  render_to_response('login.html',{"status":"用户和密码错误"})

    else:
        return render_to_response('login.html')
    """

def Host(request):
    ret = {'status':"",'data':"",'obj':""}
    if request.method == "POST":
        hostname = request.POST.get('hostname')
        ipname = request.POST.get('ip')
        groupid = request.POST.get('group')
        is_empty = all([hostname,ipname])
        print hostname,ipname,groupid,is_empty
        if is_empty:
            groupobj = GroupName.objects.get(id=groupid)
            UserName.objects.create(hostname=hostname,ip=ipname,user_group=groupobj)
        else:
            ret['status'] = "hostname和ip不能为空"
            return render_to_response('host.html',ret)

    data = UserName.objects.all()
    print data
    ret['data'] = data
    obj = UserName.objects.filter(user_group__id="1")
    ret['obj'] = obj

    print obj.query
    print type(obj)
    for itme in obj:
        print type(itme)
        print itme
    return render_to_response('host.html',ret)

def Index(request):
    return render_to_response('index.html')
