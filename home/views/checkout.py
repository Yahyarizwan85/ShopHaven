from django.views import View
from django.shortcuts import render, redirect
from home.models import Product
from home.customer import Customer
from home.order import Order


class Check_out(View):
    def get(self, request):
        if not request.session.get('customer_id'):
            return redirect('login')

        cart = request.session.get('cart', {})
        products = Product.get_products_by_id(list(cart.keys()))

        return render(request, 'checkout.html', {'products': products})

    def post(self, request):
        # Check if the customer is logged in
        if not request.session.get('customer_id'):
            return redirect('login')

        # Retrieve form data
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.session.get('customer_id')
        cart = request.session.get('cart', {})

        # Fetch products in the cart
        products = Product.get_products_by_id(list(cart.keys()))

        if not products:
            return redirect('cart_Products')  # Redirect if cart is empty

        # Process orders
        for product in products:
            order = Order(
                customer=Customer(id=customer_id),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=cart.get(str(product.id))  # Ensure key matches cart dictionary keys
            )
            order.save()

        # Clear the cart after order is placed
        request.session['cart'] = {}

        return redirect('cart_Products')
