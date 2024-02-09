from django import template

register = template.Library()


@register.filter
def classname(obj):
    return obj.__class__.__name__


@register.filter
def my_range(value):
    return range(value)


@register.filter
def substraction(value, arg):
    return value - arg
