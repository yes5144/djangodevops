# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^$', views.tasks),
    url(r'^home/$', views.home),
    url(r'^tasks/$', views.tasks),
    url(r'^record/$', views.record),
    # url(r'^get_biz_info/$', views.get_biz_info),
    url(r'^dev-guide/$', views.dev_guide),
    url(r'^contact/$', views.contact),
)
