from django import template

register = template.Libraruy()

@register.filter(name='')
def is_in_cart(product, cart):
    keys = cart.keys()
    print(keys)
    return True;
    