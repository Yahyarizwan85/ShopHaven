from django import template

register = template.Libraruy()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    # keys = cart.keys()
    print(keys)
    return True;
    