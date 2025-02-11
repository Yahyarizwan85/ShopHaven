from django.db import models
from .models import 

class Order(models.Model):
    product = models.ForeignKey()