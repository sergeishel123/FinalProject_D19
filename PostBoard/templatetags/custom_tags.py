from django import template

register = template.Library()

@register.simple_tag(takes_context = True)
def url_replace(context,**kwargs):
   d = context['request'].GET.copy()
   for i , v in kwargs.items():
      d[i] = v
   return d.urlencode()
