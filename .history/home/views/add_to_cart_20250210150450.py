from django.shortcuts import redirect
from home.models import Product

def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product')
        if not product_id:
            # If product_id is missing, you might log an error
            print("Product ID not found in POST data")
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        # Initialize the cart if it doesn't exist
        cart = request.session.get('cart', {})
        # Add or update the product in the cart
        cart[product_id] = cart.get(product_id, 0) + 1
        request.session['cart'] = cart
        request.session.modified = True  # Mark the session as modified

        return redirect('/cart')
    else:
        return redirect('/')
