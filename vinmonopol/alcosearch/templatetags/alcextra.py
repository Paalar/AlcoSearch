from django import template
from django.utils.encoding import smart_str, smart_unicode

register = template.Library()


@register.filter
def twoDec(num):
    try:
        return ("{0:.2f}".format(num))
    except:
        return 0.00


@register.filter
def removeUnderscore(text):
    try:
        output = text.replace("_", ",")
        return output
    except:
        return text


@register.filter
def title(title):
    output = str(title)
    return removeUnderscore(output)
