from django.contrib import admin

# Register your models here.
from .models import *

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('id','name','symbol','buy','sell','stock_price')
	fields = ('name','symbol','buy','sell','stock_price')

admin.site.register(Company, CompanyAdmin)

class PriceAdmin(admin.ModelAdmin):
	list_display = ('company','timestamp','stock_price')
	fields = ('company','stock_price')

#admin.site.register(Price, PriceAdmin)

class NewsAdmin(admin.ModelAdmin):
	list_display = ('id','short_news',
		'impact1','impact2','impact3',
		'impact4','impact5','impact6',
		'impact7','impact8','impact9',
		'impact10','quick_iter')
	fields = ('news_text',
		'impact1','impact2','impact3',
		'impact4','impact5','impact6',
		'impact7','impact8','impact9',
		'impact10','quick_iter')

admin.site.register(News, NewsAdmin)

class NewsPublishedAdmin(admin.ModelAdmin):
	list_display = ('id','short_news',
		'impact1','impact2','impact3',
		'impact4','impact5','impact6',
		'impact7','impact8','impact9',
		'impact10','quick_iter','iteration_counter')
	fields = ('news_text',
		'impact1','impact2','impact3',
		'impact4','impact5','impact6',
		'impact7','impact8','impact9',
		'impact10','quick_iter','iteration_counter')

#admin.site.register(NewsPublished, NewsPublishedAdmin)