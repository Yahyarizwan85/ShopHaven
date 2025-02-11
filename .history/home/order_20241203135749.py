from django.db import models

class Order(models.Model):
    product = models.Foreignk(max_length=50)