from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.views import View

class Login(View):
    def get(self, request):
        return render(request, 'login.html')  # Render the login form on GET request
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Retrieve customer by email (using Django ORM)
        user_customer = Customer.objects.filter(email=email).first()  # Use filter().first() to avoid exception
        
        if user_customer:
            # Verify the password
            if check_password(password, user_customer.password):
                request.sessions
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
