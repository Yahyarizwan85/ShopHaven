from django.shortcuts import render
from .carousel import CarouselImg

def home(request):
    # Fetch all carousel images
    carousel_images = CarouselImg.objects.all()
    return render(request, 'home.html', {'carousel_images': carousel_images})
