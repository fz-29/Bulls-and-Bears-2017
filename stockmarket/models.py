from django.db import models
from django.core.validators import MinValueValidator

# store company info, stock_price
class Company(models.Model):
    name = models.CharField(max_length=35)
    symbol = models.CharField(max_length=5)
    description = models.TextField()
    stock_price = models.DecimalField(max_digits=9, decimal_places=2, default=1000.0, validators=[MinValueValidator(0.0)])
    available_quantity = models.PositiveIntegerField(default=10000)
    total_quantity = models.PositiveIntegerField(default=10000)

    def __str__(self):
        return self.name


# to store price history for graphs
class CompanyHistory(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2,validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.company.name


# to store newsimpact
class NewsImpact(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    impact = models.FloatField(default=0.0)
    iterations_run = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.company.name


# All news
class News(models.Model):
    news_text = models.TextField()
    media = models.FileField(upload_to=None, max_length=200, null=True, blank=True)
    is_published = models.BooleanField(default = False )
<<<<<<< HEAD
    published_on = models.DateTimeField(blank=True , null=True)
=======
    published_on = models.DateTimeField(blank=True , null=True)    
>>>>>>> ae3190108d6ca634ae2c46938013d0a26a6a4b01

    def __str__(self):
        return self.news_text[:15]

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class Loan(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    amount = models.DecimalField(default=0, max_digits=15, decimal_places=2, validators=[MinValueValidator(0.0)])
    take_out_time = models.DateTimeField(auto_now_add=True)
    repay_time = models.DateTimeField(blank=True)

    def __str__(self):
        return self.customer.user.first_name

class ComplimentaryCompany(models.Model):
    company1 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='complimentary_company_1')
    company2 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='complimentary_company_2')
    factor = models.FloatField()


class SupplementaryCompany(models.Model):
    company1 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='supplementary_company_1')
    company2 = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='supplementary_company_2')
    factor = models.FloatField()

class Parameter(models.Model):
    key = models.CharField(max_length=20, null=False, blank=False, default = 'DeleteME')
    value = models.FloatField(blank=False, default = 0)

    def __str__(self):
        return self.key