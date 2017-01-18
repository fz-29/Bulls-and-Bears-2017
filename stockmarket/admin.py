from django.contrib import admin

# Register your models here.
from .models import *

class CompanyHistoryInline(admin.TabularInline):
    model = CompanyHistory

class ComplimentaryCompanyInline(admin.TabularInline):
    model = ComplimentaryCompany
    fk_name = "company1"

class SupplementaryCompanyInline(admin.TabularInline):
    model = SupplementaryCompany
    fk_name = "company1"

class CompanyAdmin(admin.ModelAdmin):
    inlines = [CompanyHistoryInline, ComplimentaryCompanyInline, SupplementaryCompanyInline]

admin.site.register(Company, CompanyAdmin)

class NewsImpactInline(admin.TabularInline):
    model = NewsImpact

class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImpactInline]

admin.site.register(News, NewsAdmin)

admin.site.register(Loan)