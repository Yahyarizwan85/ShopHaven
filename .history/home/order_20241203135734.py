from django.db import models

class Order(models.Model):
    product = models.fori(max_length=50)