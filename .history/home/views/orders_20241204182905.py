from django.views import View
from django.shortcuts import render, redirect
from home.models import Product
from home.customer import Customer
from home.order import Order
from django.contrib.auth.hashers import check_password, make_password


class Order(View):
    