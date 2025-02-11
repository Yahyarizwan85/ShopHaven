from django.db import models

class Order(models.Model):
    product = models.Foreign(max_length=50)