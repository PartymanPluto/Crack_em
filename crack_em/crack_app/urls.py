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
        url(r'^register$', views.register, name='register'),
        #url(r'^recent$', views.recent, name='recent'),
        url(r'^login$', views.user_login, name='login'),
        url(r'^login/user/(?P<username_slug>[\w\-]+)/$', views.user_account, name='myAccount'),
        #url(r'^login/user/(?P<username_slug>[\w\-]+)/creations$', views.user_creations, name='myCreations'),
        url(r'^logout$', views.user_logout, name='logout'),
        url(r'^eggs$', views.eggs, name='eggs'),
        url(r'^eggs/(?P<egg_slug>[\w\-]+)/$', 
            views.show_eggs, name='show_eggs'),
        url(r'^eggs/(?P<recipe_slug>[\w\-]+)/$', views.show_recipe, name='recipe'),
        ]