from django.db import models

class Customer(moels.Model):
    first_name = models.CharField(max_length=50)