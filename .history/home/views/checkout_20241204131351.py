from django.views import View
from django.shortcuts import render, redirect
from home.models import Product
from home.customer import Customer
from home.order import Order
from django.contrib.auth.hashers import check_password, make_password


class Check_out(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        print(address, phone, customer, cart, products)

        # Process each product in the cart and create an Order
        for product in products:
            order = Order(
                customer=Customer,
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=cart.get(str(product.id))  # Ensure the key matches session data type
            )
            order.placeOrder()  # Call the method to save the order (assuming placeOrder saves it)

        # After placing orders, redirect to 'cart_Products'
        return redirect('cart_Products')

    