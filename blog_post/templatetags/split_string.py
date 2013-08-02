from django import template
register = template.Library()

@register.filter(name="img_path_last_value")
def string_last_value(value, arg):
    last_value = value.split('/')[-1]
    return last_value
