from django.db import models

class carousel_img(models.Model):
    image = models.ImageField(upload_to='carouselimage/')
    heading = models.CharField(max_length=15)
    Para = models.TextField(max_length=35, default="", null=True, blank=True)
    
    @staticmethod
    def get_all_carousel():
        return Category.objects.all()
    
    
    def __str__(self):
        return self.heading

