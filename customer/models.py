from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import truncatechars
# Create your models here.

class StockHolding(models.Model):
    company = models.ForeignKey(stockmarket.Company, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    
class StockShorted(models.Model):
    company = models.ForeignKey(stockmarket.Company, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    
class CustomerActivity(models.Model):
	action = models.CharField(max_length=10)
	timestamp = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(validators = [MinValueValidator(0.0)],decimal_places=2, required=True)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accont_balance = models.DecimalField(default=0,max_digits=5, decimal_places=2)
    loan_balance = models.DecimalField(default=0,max_digits=5, decimal_places=2)
    stock_holdings= models.ForeignKey(StockHolding , on_delete=models.CASCADE)
    stock_shorted= models.ForeignKey(StockShorted, on_delete=models.CASCADE)

