from django import template

register = template.Library()


@register.filter
def alcoholPerLiter(literPrice, abv):
    try:
        output = literPrice * (100 / abv)
        output = ("{0:.2f}").format(output)
        return output
    except:
        return "ikke oppgitt"


@register.filter
def twoDec(num):
    try:
        return ("{0:.2f}".format(num))
    except:
        if num == "":
            return ""
        else:
            return int(num)


@register.filter
def alcoholPerPrice(price, abv):
    try:
        output = price * (100 / abv)
        output = ("{0:.2f}").format(output)
        return output
    except:
        return "ikke oppgitt"
