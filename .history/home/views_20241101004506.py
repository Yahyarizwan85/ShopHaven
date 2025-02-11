from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate, login as auth_login
from home.models import Contact, Product
from django.contrib import messages
from .category import Category
from .customer import Customer

# Create your views here.
def index(request):
    products = Product.get_all_Product()
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'About.html')  # Removed duplicate return statement

def clothes(request):
    categories = Category.get_all_category()
    categoryID = request.GET.get('category')
    products = Product.get_all_Product_by_categoryid(categoryID) if categoryID else Product.get_all_Product()
    
    data = {
        'products': products,
        'categories': categories
    }
    return render(request, 'clothes.html', data)

def contactus(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['Phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, Phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contactus.html')

def Signup(request):
    if request.method == "POST":
        print(request.POST)  # Debugging line to check form data
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if all necessary fields have data
        if first_name and last_name and phone and email and password:
            customer = Customer(first_name=first_name, last_name=last_name, email=email, phone=phone, password=password)
            customer.save()
            messages.success(request, "Signup successful!")
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'Signup.html')


def login(request):
    if request.method = "POST":
        email = request.POST['email']
        password =
    
    return render(request, 'login.html')