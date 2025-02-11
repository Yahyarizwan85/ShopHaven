from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password , check_password
from django.utils import timezone
from django.contrib import messages
from .models import Contact, Product
from .category import Category
from .customer import Customer
from 


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
        
        # Preserve entered values to repopulate the form in case of error
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }
        
        # Validation checks
        if not first_name or len(first_name) < 4:
            messages.error(request, "First name must be at least 4 characters long.")
            return render(request, 'Signup.html', {'value': value})

        if not last_name or len(last_name) < 4:
            messages.error(request, "Last name must be at least 4 characters long.")
            return render(request, 'Signup.html', {'value': value})
        
        if not phone or not phone.isdigit() or len(phone) != 11:
            messages.error(request, "Phone number must be exactly 11 digits.")
            return render(request, 'Signup.html', {'value': value})
        
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Please enter a valid email address.")
            return render(request, 'Signup.html', {'value': value})
        
        if not password or len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return render(request, 'Signup.html', {'value': value})
        
        # Check if email already exists
        if Customer.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'Signup.html', {'value': value})
        else:
            # Save the customer data if all validations pass
            customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email)
            customer.password = make_password(password)  # Hash the password before saving
            customer.save()
            messages.success(request, "Signup successful!")
            return redirect('home')  # Redirect to the home page after successful signup
    
    # Initial GET request to render the signup form
    return render(request, 'Signup.html')




def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')  # Render the login form on GET request
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Retrieve customer by email (using Django ORM)
        user_customer = Customer.objects.filter(email=email).first()  # Use filter().first() to avoid exception
        
        if user_customer:
            # Verify the password
            if check_password(password, user_customer.password):
                return redirect('home')  # Redirect to home page on successful login
            else:
                messages.error(request, "Wrong password.")  # Invalid password message
        else:
            messages.error(request, "Email or Password is invalid.")  # Invalid email or customer doesn't exist
        
        # Optional: Debugging info
        # You can remove these after debugging or use logging instead of print
        print("User found:", user_customer)
        print("Email entered:", email, "Password entered:", password)
        
        # Re-render login page with error messages
        return render(request, 'login.html')
