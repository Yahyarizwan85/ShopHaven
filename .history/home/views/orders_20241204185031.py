from django.views import View
from django.shortcuts import render, redirect
from home.models import Product
from home.customer import Customer
from home.order import Order

class Order(View):
    def get(self, request):
        customer = request.session.get('customer_id')
        orders = Order.
        return render(request, 'orders.html')