from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    """
    Checks if a product is in the cart.
    
    Args:
        product: The product object to check.
        cart: The session cart dictionary.

    Returns:
        True if the product is in the cart, False otherwise.
    """
    if not cart:
        return False  # If cart is empty or None, return False

    product_id = str(product.id)  # Ensure product ID matches the cart keys
    return product_id in cart  # Check if the product ID exists in the cart keys
