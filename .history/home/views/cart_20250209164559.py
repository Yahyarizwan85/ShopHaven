from django.views import View
from django.shortcuts import render
from home.models import Product

class Cart(View):
    def get(self, request):
        # Provide an empty dictionary as a default if 'cart' is not in the session
        cart = request.session.get('cart', {})
        # Get the list of product IDs (will be an empty list if the cart is empty)
        ids = list(cart.keys())
        # If there are no IDs, ensure products is an empty list rather than None
        products = Product.get_products_by_id(ids) if ids else []
        print(products)
        return render(request, 'cart.html', {"products": products})


