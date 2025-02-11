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
    address = models.CharField(max_length=60,default="", blank="True")
    phone = models.CharField(max_length=12,default="",blank="True")
    date = models.DateTimeField(default=now())
    
    
    def placeOrder(self):
        self.save()
        
        
    @staticmethod
    def get_orders_by_customer(customer_id):
        order.objects.filter(customer)