from django import template
from crack_app.models import Egg

register = template.Library()

@register.inclusion_tag('crack_app/egg_list.html')
def get_eggs(egg=None):
    return {'eggs': Egg.objects.all(),
            'current_egg': egg}
    