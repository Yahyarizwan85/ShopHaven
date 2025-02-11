from django import template

register = template.Library()

@register.filter(name='currency')
def currency( product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;