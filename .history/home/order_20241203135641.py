from django.db import models

class Order(models.Model):
    first_name = models.CharField(max_length=50)