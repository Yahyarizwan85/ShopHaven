from django.views import View
from django.shortcuts import render, redirect

class Check_out(View):
    def post(self, request):
        address = request.POST.get('address')
        address = request.POST.get('address')
        return redirect('cart_Products')
    