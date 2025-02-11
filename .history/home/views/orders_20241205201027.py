from django.views import View
from django.shortcuts import render, redirect
from home.models import Product
from home.customer import Customer
from home.order import Order
from home import order
from home.middleware.logguard import auth_middleware
from django.utils.decorators import method_*_

class Orders(View):
    
    @auth_middleware
    def get(self, request):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})