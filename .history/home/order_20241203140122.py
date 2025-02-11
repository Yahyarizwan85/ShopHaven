from django.db import models
from .

class Order(models.Model):
    product = models.ForeignKey()