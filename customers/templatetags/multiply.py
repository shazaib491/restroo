from django import template
register = template.Library()


@register.simple_tag()
def multiply(price, qty,*args,**kwargs):
    return price*qty
