from django import template

register = template.Library()

@register.filter(name='currency')
def is_in_cart( product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;