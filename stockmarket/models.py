from __future__ import unicode_literals
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import truncatechars
# store company info, stock_price
class Company(models.Model):
    name = models.CharField(max_length=35)
    symbol = models.CharField(max_length=40)
    description = models.TextField()
    stock_price = models.FloatField(default=1000.0, validators=[MinValueValidator(0.0)])
    availquantity = models.PositiveIntegerField(default=10000)
    totlaquantity = models.PositiveIntegerField(default=10000)

    def __unicode__(self):
        return self.name


# to store price history for graphs
class CompanyHistory(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(validators=[MinValueValidator(0.0)])

    def __unicode__(self):
        return self.company.name


# to store newsimpact
class NewsImpact(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    Impact = models.FloatField()

    def __unicode__(self):
        return self.company.name


# news yet to be issued
class News(models.Model):
    news_text = models.CharField(max_length=500)
    media = FileField(upload_to=None, max_length=200)
    Newsimpact = ForeignKey('NewsImpact', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.news_text[:35]

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class Loan(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    Amount = models.FloatField(default=0.0)
    TakeOutTime = models.DateTimeField(auto_now_add=False)
    RepayTime = models.DateTimeField(auto_now_add=False)


# have to write a unicode function after getting info about customer model

class ComplimentaryCompanies(models.Model):
    company1 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='complimentary_company_1')
    company2 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='complimentary_company_2')
    factor = models.FloatField(validators=[MinValueValidator(0.0)])


class SupplementaryCompanies(models.Model):
    company1 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='supplementary_company_1')
    company2 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='supplementary_company_2')
    factor = models.FloatField(validators=[MinValueValidator(0.0)])
