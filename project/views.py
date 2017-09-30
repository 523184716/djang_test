# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import  HttpResponse
from django.shortcuts import render,render_to_response
import sys
reload(sys)
sys
def index(request):
    return  HttpResponse('Hello ,world')

def login(request):
    return render_to_response('login.html')
from django.shortcuts import render

# Create your views here.
