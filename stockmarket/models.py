from __future__ import unicode_literals
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import truncatechars
# store company info, stock_price
class Company(models.Model):
    name = models.CharField(max_length=35)
    symbol = models.CharField(max_length=40)
    description = models.TextField()
    stock_price = models.DecimalField(max_digits=9, decimal_places=2, default=1000.0, validators=[MinValueValidator(0.0)])
    available_quantity = models.PositiveIntegerField(default=10000)
    total_quantity = models.PositiveIntegerField(default=10000)

    def __str__(self):
        return self.name


# to store price history for graphs
class CompanyHistory(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(default=0,max_digits=9, decimal_places=2,validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.company.name


# to store newsimpact
class NewsImpact(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    impact = models.DecimalField(default=0,decimal_places=2)

    def __str__(self):
        return self.company.name


# news yet to be issued
class News(models.Model):
    news_text = models.TextField()
    media = models.FileField(upload_to=None, max_length=200)
    news_impact = models.ForeignKey('NewsImpact', on_delete=models.CASCADE)

    def __str__(self):
        return self.news_text[:35]

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class Loan(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    amount = models.DecimalField(default=0,max_digits=15, decimal_places=2,validators=[MinValueValidator(0.0)])
    take_out_time = models.DateTimeField(auto_now_add=True)
    repay_time = models.DateTimeField(auto_now_add=False,blank=True)


# have to write a unicode function after getting info about customer model

class ComplimentaryCompanies(models.Model):
    company1 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='complimentary_company_1')
    company2 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='complimentary_company_2')
    factor = models.DecimalField(validators=[MinValueValidator(0.0)])


class SupplementaryCompanies(models.Model):
    company1 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='supplementary_company_1')
    company2 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='supplementary_company_2')
    factor = models.DecimalField(validators=[MinValueValidator(0.0)])
