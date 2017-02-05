# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.utils import timezone
from math import exp
from .models import *
from random import uniform

import datetime


@shared_task
def revise_stock_price_by_news():
	'''
		This function will revise Stock Prices of companies due to (newsImpact, company)

		UPDATE 1
	'''	
	#fetch constants
	increment_factor_1 = Parameter.objects.get(key = 'increment_factor_1').value #0.03
	increment_factor_2 = Parameter.objects.get(key = 'increment_factor_2').value #0.01
	decrement_factor_1 = Parameter.objects.get(key = 'decrement_factor_1').value
	decrement_factor_2 = Parameter.objects.get(key = 'decrement_factor_2').value
	impact_growth_iter = Parameter.objects.get(key = 'impact_growth_iter').value #set it to 1

	control_update_1 = Parameter.objects.get(key = 'control_update_1').value

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
				sp_t = sp_t + sp_t * control_update_1 *(impact*increment_factor_1*(exp(a*t)))
			else:
				sp_t = sp_t + sp_t * control_update_1 *(impact*increment_factor_2*(exp(-a*0.5*t)))
		elif impact < 0: #decrease stock price
			if t <= impact_growth_iter:
				sp_t = sp_t - sp_t * control_update_1 *(impact*increment_factor_1*(exp(a*t)))
			else:
				sp_t = sp_t - sp_t * control_update_1 *(impact*increment_factor_2*(exp(-a*0.5*t)))
		#updates
		impact_info.iterations_run = t + 1
		company.stock_price = sp_t
		company.save()
		impact_info.save()

	#update history and random noise
	#revise_stock_price_random()


@shared_task
def revise_stock_price_by_stocks():
	'''
		This function will revise Stock Prices of companies due effects of stock count, stock
		prices of complementary and supplementary company
	
		UPDATE 2
	'''	
	#Iterate on all companies
	control_update_2 = Parameter.objects.get(key = 'control_update_2').value
	c_delta_update_2 = Parameter.objects.get(key = 'c_delta_update_2').value
	stock_ratio_to_value = Parameter.objects.get(key = 'stock_ratio_to_value').value
	try:
		all_companies = Company.objects.all()
		for company in all_companies:
			price = float(company.stock_price)

			#Changes due to 3 components
			# Quantity of Stocks
			# Stock Price of Supplementary and Complementary Company
			F1 = F2 = F3 = 0.0
					
			#query quantity
			histories = CompanyHistory.objects.filter(company=company).order_by('timestamp').reverse()
			
			if len(histories) >= c_delta_update_2 :
				# We have sufficient data for delta calc
				# Quantity of Stocks
				s1 = histories[0].stocks_available
				s0 = histories[c_delta_update_2 - 1].stocks_available
				try:
					if s1 > s0: #stock demand decreased
						F1 = -((s1*1.0)/s0) * stock_ratio_to_value
					else:
						F1 = +((s0*1.0)/s1) * stock_ratio_to_value
				except:
					pass

				# Stock Price of Complementary Company

				# Stock Price of Supplementary Company
				print F1
				price = price + price * control_update_2 * (F1 + F2 + F3)
				company.stock_price = price
				company.save()
	except:
		pass

	#update history and random noise
	#revise_stock_price_random()

@shared_task
def revise_stock_price_random():
	'''
		This function will revise Stock Prices of companies due effects of stock count, stock
		prices of complementary and supplementary company
	
		UPDATE 3
	'''
	control_update_3 = Parameter.objects.get(key = 'control_update_3').value
	all_companies = Company.objects.all()
	for company in all_companies:
		price = float(company.stock_price)
		price = price * (1 + (control_update_3*uniform(-1.0,1.0)))
		company.stock_price = price
		company.save()

		hist = CompanyHistory(company = company, price = price, stocks_available = company.available_quantity)
		hist.save()

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
	#load interest rate
	interest_rate = Parameter.objects.get(key = 'interest_rate').value#per iteration of 15min

	#get all loan entries
	loan_entries = Loan.objects.all()

	for entry in loan_entries:
		new_amount = float(entry.amount) * (1.0 + interest_rate)
		entry.amount = new_amount
		entry.save()
