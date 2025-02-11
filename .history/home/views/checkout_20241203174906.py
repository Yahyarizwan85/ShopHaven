from django.views import View
from django.shortcuts import render, redirect

class Check_out(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        pr
        return redirect('cart_Products')
    