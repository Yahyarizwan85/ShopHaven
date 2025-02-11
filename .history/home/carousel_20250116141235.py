from django.db.utils import OperationalError
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def carousel_home(request):
    try:
        carousel_images = carousel_img.objects.all()
    except OperationalError as e:
        logger.error(f"Database error fetching carousel images: {e}")
        return render(request, 'home.html', {'database_error': True})
    # ... rest of the code