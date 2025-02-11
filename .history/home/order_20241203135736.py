from django.db import models

class Order(models.Model):
    product = models.forign(max_length=50)