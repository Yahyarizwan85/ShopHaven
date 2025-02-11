from django.views import View
from django.shortcuts import render
from home.models import Product

class Cart(View):
    def get(self, request):
        # Ensure the cart key exists in the session.
        if 'cart' not in request.session:
            request.session['cart'] = {}
        
        cart = request.session['cart']
        # Convert cart keys to a list. If cart is empty, this will be an empty list.
        ids = list(cart.keys())
        # Use a conditional to handle empty ids.
        products = Product.get_products_by_id(ids) if ids else []
        return render(request, 'cart.html', {"products": products})
