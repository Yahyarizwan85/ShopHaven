from django.db import models
from .models import Product
from .customer import Customer
from django.utils.timezone import now  

class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    adress = models.CharField(=100)
    phone = models.CharField(max_length=11)
    date = models.DateTimeField(default=now())
    