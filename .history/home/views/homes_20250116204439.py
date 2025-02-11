from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.views import View
from home.models import Contact, Product
from home.category import Category
from home.carousel import CarouselImg


def index(request):
    """Displays all products on the homepage."""
    products = Product.get_all_Product()
    return render(request, 'index.html', {'products': products })


def about(request):
    """Renders the About page."""
    return render(request, 'about.html')  

class Clothes(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove') 
        cart = request.session.get('cart', {}) 
        
        if product:
            quantity = cart.get(product, 0)  # Get the current quantity in the cart
            if remove:  # If removing an item
                if quantity <= 1:
                    cart.pop(product, None)  # Remove the product from the cart
                else:
                    cart[product] = quantity - 1  # Decrease quantity
            else:  # Adding an item
                cart[product] = quantity + 1

            request.session['cart'] = cart  # Save updated cart to session
            print('Cart:', request.session['cart'])  # Debugging output for testing
        
        return redirect('clothes')  

    def get(self, request):
        categories = Category.get_all_category()  # Fetch all categories
        category_id = request.GET.get('category')  # Get selected category ID
        products = Product.get_all_Product_by_categoryid(category_id) if category_id else Product.get_all_Product()
        cart = request.session.get('cart', {})  # Fetch cart from session
        context = {
            'products': products,
            'categories': categories,
            'cart': cart,
        }
        return render(request, 'clothes.html', context)


def contact_us(request):
    """Handles contact form submissions."""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if all([name, email, phone, desc]):
            contact = Contact(
                name=name,
                email=email,
                phone=phone,
                desc=desc,
                date=timezone.now()
            )
            contact.save()
            messages.success(request, "Your message has been sent!")
        else:
            messages.error(request, "Please fill in all fields.")
    return render(request, 'contactus.html')
