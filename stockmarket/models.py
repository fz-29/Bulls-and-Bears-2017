from __future__ import unicode_literals
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import truncatechars

#store company info, stock_price 
class Company(models.Model):
	name = models.CharField(max_length=35)
	symbol = models.CharField(max_length=4)
	buy = models.PositiveIntegerField(default=1000000)
	sell = models.PositiveIntegerField(default=1000000)
	stock_price = models.FloatField(default=1000.0)

	def __unicode__(self):
		return self.name

#to store price history for graphs
class Price(models.Model):
	company = models.ForeignKey('Company', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	stock_price = models.FloatField()
	
	def __unicode__(self):
		return self.company.name

#news yet to be issued
class News(models.Model):
	news_text = models.CharField(max_length=500)
	impact1 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(-5)])
	impact2 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(-5)])
	impact3 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(-5)])
	impact4 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(-5)])
	impact5 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(-5)])
	impact6 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(-5)])
	impact7 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(-5)])
	impact8 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(-5)])
	impact9 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(-5)])
	impact10 = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(-5)])
	#number of iterations for which factor grows exponentially, after those no. of iterations it decays exponentially
	quick_iter = models.PositiveIntegerField(default=5, validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
	def __unicode__(self):
		return self.news_text[:35]

	@property
	def short_news(self):
		return truncatechars(self.news_text, 30)

	class Meta:
         verbose_name = "News"
         verbose_name_plural = "News"

#news issued so far
class NewsPublished(models.Model):
	news_text = models.CharField(max_length=500)
	impact1 = models.IntegerField(default=0)
	impact2 = models.IntegerField(default=0)
	impact3 = models.IntegerField(default=0)
	impact4 = models.IntegerField(default=0)
	impact5 = models.IntegerField(default=0)
	impact6 = models.IntegerField(default=0)
	impact7 = models.IntegerField(default=0)
	impact8 = models.IntegerField(default=0)
	impact9 = models.IntegerField(default=0)
	impact10 = models.IntegerField(default=0)
	#number of iterations for which factor grows exponentially
	quick_iter = models.PositiveIntegerField(default=5, validators=[MaxValueValidator(5),MinValueValidator(0)])
	iteration_counter = models.PositiveIntegerField(default=0)
	def __unicode__(self):
		return self.news_text[:35]

	@property
	def short_news(self):
		return truncatechars(self.news_text, 30)

	class Meta:
         verbose_name = "News Published"
         verbose_name_plural = "News Published"