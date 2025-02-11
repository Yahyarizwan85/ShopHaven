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
        return redirect('cart_Products')
    
    for product in products:
        order = Order(customer = customer,
                      product)
    
    return redirect('cart_Products')
    