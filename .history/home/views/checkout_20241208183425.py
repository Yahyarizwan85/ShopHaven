from django.views import View
from django.shortcuts import render, redirect
from home.models import Product
from home.customer import Customer
from home.order import Order
from django.contrib.auth.hashers import check_password, make_password
from home.middleware.logguard import auth_middleware


class Check_out(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        print(address, phone, customer, cart, products)
        
        if user_customer not in Login:
            return redirect*
        
        for product in products:
            order = Order(
                customer=Customer(id=customer),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=cart.get(str(product.id))  # Ensure the key matches session data type
            )
            order.save()
            request.session['cart'] = {}

        # After placing orders, redirect to 'cart_Products'
        return redirect('cart_Products')

    