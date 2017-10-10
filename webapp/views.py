# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import utils
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from  django.http import  HttpResponse
from  .forms import  RegisterForm
from . import forms
from .models import  Asset,Userinfo,UserName,GroupName,ZabbixGroup,ZabbixUser
import json
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
            ##delete
            #UserName.objects.filter(hostname=hostname).delete()
            ##update
            #UserName.objects.filter(hostname=hostname).update(ip='8.8.8.8')
        else:
            ret['status'] = "hostname和ip不能为空"
            return render_to_response('host.html',ret)

    data = UserName.objects.all()
    print data
    ret['data'] = data
    ###联表查询，user_group是第二个表的外键，连接第二张表的id做判断，小于3的全部查询返回
    #obj = UserName.objects.filter(user_group__id__lt="3")
    ###同上，联表查询，包含关系,values 去某个字段的值
    obj = UserName.objects.filter(user_group__groupname__contains="业务").values('hostname')
    ret['obj'] = obj

    print obj.query
    print type(obj)
    for itme in obj:
        print type(itme)
        print itme
    return render_to_response('host.html',ret)

def Index(request):
    return render_to_response('index.html')

###多对多往第三张表插入数据
def Many(request):
    u1 = ZabbixUser.objects.get(id=1)
    g1 = ZabbixGroup.objects.get(id=2)
    g1.relation.add(u1)    ###两种方式，第一个是有直接设置many to many字段的表添加另外一张
    #ur.zabbixgroup_set.add(g1)    ###这种事没有那个字段的直接对象点那张表名，然后_set.add添加另外表的一个对象

    ###图片上传属性
    return HttpResponse('ok')


def FormLogin(request):
    ret = {"obj":None,"error":""}
    obj = forms.ALogin()
    ret['obj'] = obj
    if request.method == "POST":
        check_request = forms.ALogin(request.POST)
        check_result = check_request.is_valid()
        if check_result:
            pass
        else:
            errorobj = check_request.errors
            print type(errorobj)

            errorresult =  errorobj.as_data().values()[0][0][0]
            print errorresult.encode("utf-8")
            ret['error'] = errorresult
            ret['obj'] = check_request

    return render_to_response('login.html', ret)

def TextModelForm(request):
    ret = {"obj":None,"error":""}
    obj = forms.Aloginmodelform()
    ret['obj'] = obj
    if request.method == "POST":
        check_request = forms.Aloginmodelform(request.POST)
        check_result = check_request.is_valid()
        if check_result:
            pass
        else:
            errorobj = check_request.errors
            print type(errorobj)

            errorresult =  errorobj.as_data().values()[0][0][0]
            print errorresult.encode("utf-8")
            ret['error'] = errorresult
            ret['obj'] = check_request

    return render_to_response('login.html', ret)

def Ajax(request):
    ret = {"status":""}
    if request.method == "POST":
        # result = request.POST.get('name')
        # if result:

        print request.POST
        data = {'status':'ok','msg':'请求成功','data':[1,2,2,3,4]}
        return  HttpResponse(json.dumps(data))
        # else:
        #     ret['status'] = "请填入数据"
        #     return HttpResponse(json.dumps(ret))

    return render_to_response('login.html',ret)