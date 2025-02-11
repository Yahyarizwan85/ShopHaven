from django.shortcuts import render
from .carousel import CarouselImg

def home(request):
    # Fetch all carousel images
    carousel_images = CarouselImg.get_all_carousel()
    return render(request, 'home.html',)
