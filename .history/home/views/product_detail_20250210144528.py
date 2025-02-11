# In views/product_detail.py

from django.shortcuts import render, get_object_or_404
from home.models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # For recommendations, e.g., products in the same category
    recommended_products = Product.objects.filter(category=product.category).exclude(id=product_id)[:4]
    return render(request, 'product_detail.html', {
        'product': product,
        'recommended_products': recommended_products,
    })
