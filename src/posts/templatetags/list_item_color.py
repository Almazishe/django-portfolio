from django import template

register = template.Library()


@register.simple_tag()
def max_height(queryset):
    return queryset.count() * 400