# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.utils import timezone
from math import exp
from .models import *

import datetime


@shared_task
def revise_stock_price_by_news():
	'''
		This function will revise Stock Prices of companies due to (newsImpact, company)
	'''	
	#fetch constants
	increment_factor_1 = Parameter.objects.get(key = 'increment_factor_1').value #0.03
	increment_factor_2 = Parameter.objects.get(key = 'increment_factor_2').value #0.01
	decrement_factor_1 = Parameter.objects.get(key = 'decrement_factor_1').value
	decrement_factor_2 = Parameter.objects.get(key = 'decrement_factor_2').value
	impact_growth_iter = Parameter.objects.get(key = 'impact_growth_iter').value #set it to 1

	#Iterate on (impact,company) of news which are published so far
	published_news_impacts = NewsImpact.objects.filter(news__is_published=True)
	
	for impact_info in published_news_impacts:
		impact = impact_info.impact
		company =  impact_info.company

		t = impact_info.iterations_run
		
		sp_t = float(company.stock_price)

		a = (1.0/impact)

		if impact > 0: #increase stock price
			if t <= impact_growth_iter:
				sp_t = sp_t + sp_t * (impact*increment_factor_1*(exp(a*t)))
			else:
				sp_t = sp_t + sp_t * (impact*increment_factor_2*(exp(-a*0.5*t)))
		elif impact < 0: #decrease stock price
			if t <= impact_growth_iter:
				sp_t = sp_t - sp_t * (impact*increment_factor_1*(exp(a*t)))
			else:
				sp_t = sp_t - sp_t * (impact*increment_factor_2*(exp(-a*0.5*t)))
		#updates
		impact_info.iterations_run = t + 1
		company.stock_price = sp_t
		company.save()
		impact_info.save()



@shared_task
def revise_stock_price_by_company():
	'''
		This function will revise Stock Prices of companies due effects of stock count, stock
		prices of complementary and supplementary company
	'''	
	#Iterate on all companies
	pass

@shared_task
def publish_by_exact_time():
	#Iterate on all news
	to_publish = News.objects.filter(is_published=False)
	now = timezone.now()
	for news in to_publish:
		if now >= news.published_on:
			news.is_published = True
			news.save()

@shared_task
def publish_by_interval():
	'''
		This task can be used when we decide to dispatch news ONE BY ONE on REGULAR interval
	'''
	to_publish_news = News.objects.filter(is_published=False).earliest('published_on')
	to_publish_news.is_published = True
	to_publish_news.save()

@shared_task
def update_loan_interest():
	'''
		This function will recalculate the interest on the amount left for repayment.
		Use interest rate from Parameter model
	'''
	pass
