# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 16:40:02 2019

@author: thero
"""

from django import template
from crack_app.models import Egg, Recipe

register = template.Library()

@register.inclusion_tag('crack_em/egg_list.html')
def get_eggs(egg=None):
    return {'eggs': Egg.objects.all(),
            'current_egg': egg}
    