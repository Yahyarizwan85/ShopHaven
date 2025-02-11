from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Product, 
from django.contrib import messages
from .category import Category

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
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        
        customer = Customer(first_name=first_name, last_name=last_name, email=email, phone=phone, password=password)
        customer.save()        
    return render(request, 'Signup.html')
