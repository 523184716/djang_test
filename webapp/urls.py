#coding:utf-8

from django.conf.urls import  url
from .views import  List,Add,Delete,Update,Query,AseetList,Login,Register

urlpatterns = [
    # url(r'^$',views.List,name='index'),
    # url(r'^(?P<name>\d*)/(?P<id>\d*)/$',views.List),
    # url(r'^(?P<name>\d*)/$',views.List,{'id':222})
    url(r'^add/(?P<name>\d*)/$',Add),
    url(r'^delete/(?P<id>\d*)/$',Delete),
    url(r'^update/(?P<id>\d*)/(?P<hostname>\w*)/$',Update),
    url(r'^query/(?P<hostname>\w*)/$',Query),
    url(r'^aseetList/$',AseetList),
    url(r'^login/$',Login),
    url(r'^register/$',Register),

]