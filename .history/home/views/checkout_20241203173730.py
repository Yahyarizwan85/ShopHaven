from django.views import View
from django.shortcuts import render, redirect

class Check_out(View):
    def post(self, request):
        add(request.POST)
        return redirect('cart_Products')
    