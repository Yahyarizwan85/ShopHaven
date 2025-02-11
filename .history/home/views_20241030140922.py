from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from .models import Product
from .category import Category

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is Muhammad Yahya Rizwan")

def about(request):
    return render(request, 'About.html')
    return HttpResponse("This is ABout page")
    
def clothes(request):
    products = Product.get_all_Product();
    categories = Category.get
    return render(request, 'clothes.html', {'products': products})


def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        Phone = request.POST['Phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, Phone=Phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your Message has been sent!.")
    return render(request, 'contactus.html')