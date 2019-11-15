"""learning_logs的urls.py"""
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
]