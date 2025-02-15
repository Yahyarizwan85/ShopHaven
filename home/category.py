from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    
    @staticmethod
    def get_all_category():
        return Category.objects.all()
    
    def __str__(self):
            return self.name