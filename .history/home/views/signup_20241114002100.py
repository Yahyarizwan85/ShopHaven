from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.contrib import messages
from .customer import Customer
from django.views import View




class Signup(View):
    def get(self, request):
        return render(request, 'Signup.html')
    
    def post(self, request):
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
        
        # Re-render the signup page in case of any failure
        return render(request, 'Signup.html')
