""" learning_logs   URL """
__author__ = 'Bryan'
#coding=utf8

from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^topics/$', views.topics, name='topics'),
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]


