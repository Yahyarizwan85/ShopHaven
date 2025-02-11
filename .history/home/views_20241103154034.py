from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact, Product
from .category import Category
from .customer import Customer


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


def signup(request):
    """Handles user signup with input validation."""
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Validate that all fields are filled
        if all([first_name, last_name, phone, email, password]):
            # Check if email already exists
            if Customer.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email)
                customer.set_password(password)  # Securely hash the password
                customer.save()
                messages.success(request, "Signup successful!")
                return redirect('login')
        else:
            messages.error(request, "Please fill in all required fields.")

    return render(request, 'Signup.html')


def login(request):
    """Handles user login and authenticates credentials."""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate the user
        try:
            customer = Customer.objects.get(email=email)
            if customer.check_password(password):  # Securely check the password
                auth_login(request, customer)
                messages.success(request, "Login successful!")
                return redirect('index')
            else:
                messages.error(request, "Invalid email or password.")
        except Customer.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            
    return render(request, 'login.html')
