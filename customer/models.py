from django.core.validators import MinValueValidator
from django.conf import settings
from django.db import models
# Create your models here.

class StockHolding(models.Model):
    company = models.ForeignKey("stockmarket.Company", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.customer.user.first_name
    
class StockShorted(models.Model):
    company = models.ForeignKey("stockmarket.Company", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.customer.user.first_name
    
class CustomerActivity(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    action = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2, validators=[MinValueValidator(0.0)])
    
    def __str__(self):
        return self.customer.user.first_name

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    accont_balance = models.DecimalField(default=0, max_digits=15, decimal_places=2, validators=[MinValueValidator(0.0)])
    loan_balance = models.DecimalField(default=0, max_digits=15, decimal_places=2, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return user.first_name