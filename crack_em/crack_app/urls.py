# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:59:42 2019

@author: thero
"""

from django.conf.urls import url
from crack_app import views

urlpatterns = [
        url(r'^$', views.home, name='home'),
        url(r'^home/$', views.home, name='home'),
        url(r'^about/$', views.about, name='about'),
        url(r'^contact/$', views.contact, name='contact'),
        url(r'^FAQ/$', views.FAQ, name='FAQ'),
        url(r'^eggs/$', views.eggs, name='eggs'),
        url(r'^eggs/(?P<egg_slug>[\w\-]+)/$', 
            views.show_egg, name='show_egg'),
        url(r'^recipe/(?P<recipe_slug>[\w\-]+)/$', views.show_recipe, name='recipe'),
        url(r'^add_recipe/$', views.add_recipe, name='add_recipe'),
        url(r'^user/(?P<username>[\w\-]+)/$', views.user_account_page, name='profile'),
        url(r'^register_profile/$', views.register_profile, name='register_profile'),
        url(r'^like/$', views.like_user, name='like_user'),
        url(r'^rate/$', views.rate_recipe, name= 'rate recipe'),
        ]