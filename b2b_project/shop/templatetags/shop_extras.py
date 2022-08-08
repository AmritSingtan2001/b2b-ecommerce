from django import template

register = template.Library()

@register.filter(name='dict_key')
def dict_key(d, key):    
   return d[key]