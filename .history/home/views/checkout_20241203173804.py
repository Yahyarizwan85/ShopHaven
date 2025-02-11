from django.views import View
from django.shortcuts import render, redirect

class Check_out(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        return redirect('cart_Products')
    