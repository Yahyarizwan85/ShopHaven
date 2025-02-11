from .carousel import carousel_img
from django.shortcuts import render, redirect

import logging

logger = logging.getLogger(__name__)  # Get a logger instance

def carousel_home(request):
    carousel_images = carousel_img.objects.all()
    logger.debug(f"Fetched carousel images: {carousel_images}") # Log the queryset
    return render(request, 'home.html', {'carousel_images': carousel_images})