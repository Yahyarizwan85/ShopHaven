from django.views import View
from django.shortcuts import render, redirect
from home.models import Product
from home.customer import Customer
from home.order import Order

class Order(View):
    def get(self, request):
        customer = request.session.def get_context_data(self, **kwargs) -> dict[str, Any]:
            context = super().get_context_data(**kwargs)
            context[""] = 
            return context
        
        return render(request, 'orders.html')