from django import template

register = template.Library()

@register.simple_tag()
def get_color(index):
    if index % 4 == 0:
        return 'secondary'
    if index % 3 == 0:
        return 'primary'
    if index % 2 == 0:
        return 'danger'
    return 'dark'

@register.simple_tag()
def max_height(queryset):
    return queryset.count() * 300