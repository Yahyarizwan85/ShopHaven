from django.db import models

class Order(models.Model):
    product = models.CharField(max_length=50)