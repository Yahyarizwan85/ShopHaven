from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from .models import Product
from .category import Category

# Create your views here.
def index(request):
    products = Product.get_all_Product()
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'About.html')
    return HttpResponse("This is ABout page")
    
def clothes(request):
    products = None
    categories = Category.get_all_category()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_Product_by_categoryid(categoryID)
    else:
        products = Product.get_all_Product(); 
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'clothes.html', data)


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



def Signup(request):
        if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

    return render(request, 'Signup.html')
    