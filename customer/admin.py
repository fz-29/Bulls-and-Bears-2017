from django.contrib import admin
from customer.models import *
from stockmarket.models import *

# Register your models here.
class CustomerActivityInline(admin.TabularInline):
    model = CustomerActivity

class StockHoldingInline(admin.TabularInline):
    model = StockHolding

class StockShortedInline(admin.TabularInline):
    model = StockShorted

class LoanInline(admin.TabularInline):
    model = Loan

class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomerActivityInline, StockHoldingInline, StockShortedInline, LoanInline]

admin.site.register(Customer, CustomerAdmin)