from __future__ import unicode_literals
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import truncatechars
# Create your models here.

class StockHolding(models.Model):
    company = models.ForeignKey("stockmarket.Company", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.customer
    
class StockShorted(models.Model):
    company = models.ForeignKey("stockmarket.Company", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.customer
    
class CustomerActivity(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
	action = models.CharField(max_length=10)
	timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecmalFeild(default=0,max_digits=9, decimal_places=2,validators=[MinValueValidator(Decimal('0.00'))])
    
    def __str__(self):
        return self.customer

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    accont_balance = models.DecimalField(default=0,max_digits=15, decimal_places=2)
    loan_balance = models.DecimalField(default=0,max_digits=15, decimal_places=2)
    stock_holdings= models.ForeignKey(StockHolding , on_delete=models.CASCADE)
    stock_shorted= models.ForeignKey(StockShorted, on_delete=models.CASCADE)
     def __str__(self):
        return user.first_name
    
