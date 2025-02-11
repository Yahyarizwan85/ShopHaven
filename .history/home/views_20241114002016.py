from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from django.contrib import messages
from .models import Contact, Product
from .category import Category
from .customer import Customer
from django.views import View


def index(request):
    """Displays all products on the homepage."""
    products = Product.get_all_Product()
    return render(request, 'index.html', {'products': products})


def about(request):
    """Renders the About page."""
    return render(request, 'About.html')  


def clothes(request):
    """Displays products filtered by selected category."""
    categories = Category.get_all_category()
    category_id = request.GET.get('category')
    products = Product.get_all_Product_by_categoryid(category_id) if category_id else Product.get_all_Product()
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'clothes.html', context)


def contactus(request):
    """Handles contact form submissions."""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('Phone')
        desc = request.POST.get('desc')
        
        if all([name, email, phone, desc]):
            contact = Contact(name=name, email=email, Phone=phone, desc=desc, date=timezone.now())
            contact.save()
            messages.success(request, "Your message has been sent!")
        else:
            messages.error(request, "Please fill in all fields.")
    return render(request, 'contactus.html')




