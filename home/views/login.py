from django.shortcuts import render, redirect , HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.views import View
from home.customer import Customer  # Ensure this model is correctly imported


class Login(View):
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        """Render the login form on a GET request."""
        return render(request, 'login.html')

    def post(self, request):
        """Handle login logic on a POST request."""
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Retrieve the customer by email
        user_customer = Customer.objects.filter(email=email).first()

        if user_customer:
            # Check the provided password against the hashed password in the database
            if check_password(password, user_customer.password):
                # Save the user's information in the session
                request.session['customer_id'] = user_customer.id
                request.session['email'] = user_customer.email
                messages.success(request, "Logged in successfully!")
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('home')
            else:
                # Invalid password
                messages.error(request, "Invalid password.")
        else:
            # No customer found with the given email
            messages.error(request, "Invalid email or password.")

        # Re-render the login page with error messages
        return render(request, 'login.html')


def logout(request):
    request.session.clear()
    return redirect('login')