from django.db import models

class Order(models.Model):
    product = models.For(max_length=50)