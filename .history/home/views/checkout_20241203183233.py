from django.views import View
from django.shortcuts import render, redirect
from . import 

class Check_out(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, products)
        return redirect('cart_Products')
    