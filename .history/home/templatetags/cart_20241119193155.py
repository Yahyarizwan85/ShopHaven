from django import template

register = template.Libraruy()

@register.filter
def is_in_cart(product, cart):
    keys = cart.keys()
    print(keys)
    return True;
    