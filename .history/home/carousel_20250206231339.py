from django.db import models

class CarouselImg(models.Model):  # Use PascalCase for the model name
    image = models.ImageField(upload_to='img/%/')
    heading = models.CharField(max_length=15)
    Para = models.TextField(max_length=35, default="", null=True, blank=True)
    
    @staticmethod
    def get_all_carousel():
        return CarouselImg.objects.all()
    
    def __str__(self):
        return self.heading
