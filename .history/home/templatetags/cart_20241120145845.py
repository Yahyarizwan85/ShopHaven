from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart( product, cart):
    keys = cart.keys()
    for id in keys:
        if id == product.id
    print(product)
    return True;
    

