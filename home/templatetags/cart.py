from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart( product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;
    
@register.filter(name='cart_quantity')
def cart_quantity( product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;

@register.filter(name='Total_cart_Price')
def Total_cart_Price(product, cart):
    return product.price * cart_quantity(product, cart)

@register.filter(name='total_cart')
def total_cart(products, cart):
    total = 0
    for p in products:
        total += Total_cart_Price(p, cart)  # Add each product's total price to `total`
    return total  # Return after the loop is completed


