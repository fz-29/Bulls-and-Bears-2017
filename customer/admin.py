from django.contrib import admin
from customer.models import *

# Register your models here.
class CustomerActivityInline(admin.TabularInline):
    model = CustomerActivity

class StockHoldingInline(admin.TabularInline):
    model = StockHolding

class StockShortedInline(admin.TabularInline):
    model = StockShorted

class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomerActivityInline, StockHoldingInline, StockShortedInline]

admin.site.register(Customer, CustomerAdmin)