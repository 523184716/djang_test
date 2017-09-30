#coding:utf-8

from  django import  template
# from django.template.base import resolve_variable, Node, TemplateSyntaxError
# from  django.template.base import
register = template.Library()

@register.simple_tag
def mymethod(v1):
    result = v1 * 1000
    return  result