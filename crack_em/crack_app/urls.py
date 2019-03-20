# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:59:42 2019

@author: thero
"""

from django.conf.urls import url
from crack_app import views

urlpatterns = [
        url(r'^$', views.home, name='home'),
        url(r'^home$', views.home, name='home'),
        url(r'^about$', views.about, name='about'),
        url(r'^contact$', views.contact, name='contact'),
        url(r'^FAQ$', views.FAQ, name='FAQ'),
        url(r'^eggs$', views.eggs, name='eggs'),
        url(r'^eggs/(?P<egg_slug>[\w\-]+)/$', 
            views.show_eggs, name='show_eggs'),
        url(r'^eggs/(?P<recipe_slug>[\w\-]+)/$', views.show_recipe, name='recipe'),
        url(r'^user/(?P<username_slug>[\w\-]+)/$', views.user_account_page, name='myAccount'),
        url(r'^like/$', views.like_recipe, name='like recipe'),
        url(r'^rate/$', views.rate_recipe, name= 'rate recipe'),
        ]