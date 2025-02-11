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
    adress = models.CharField(max_length=100)
    phone = models.IntegerField(=)
    date = models.DateTimeField(default=now())
    