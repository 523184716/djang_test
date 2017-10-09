# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import  models

class UserType(models.Model):
    name = models.CharField(max_length=20)

class Userinfo(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    gender = models.BooleanField(default=False)
    Age = models.IntegerField(default=19)
    memo = models.TextField(default='xxaa')
    createDate = models.DateTimeField(default='2017-08-05 12:12')
    TypeId = models.ForeignKey('UserType')     #多对一关系
    #onetooen = models.OneToOneField('UserType')   #一对一关系



class ZabbixUser(models.Model):
    name = models.CharField(max_length=50)

class ZabbixGroup(models.Model):
    name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=50)
    relation = models.ManyToManyField('ZabbixUser')   #多对多关系

class Asset(models.Model):
    hostname = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)

class Temp(models.Model):
    Gender_choice =(
        (u'1',u'管理员'),
        (u'2',u'普通用户'),
        (u'3', u'超级管理员'),
    )
    userType = models.CharField(max_length=20,choices=Gender_choice,default=1)

class UserName(models.Model):
    hostname = models.CharField(max_length=30)
    ip = models.CharField(max_length=30)
    #usertype = models.ForeignKey('UserType')
    user_group = models.ForeignKey('GroupName')

    def __unicode__(self):
        temp = "当前username包含的对象(%s,%s)" % (self.hostname,self.ip)
        return temp

class GroupName(models.Model):
    groupname = models.CharField(max_length=50)
    #user_group = models.ManyToManyField('UserName')