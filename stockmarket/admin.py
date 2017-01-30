from django.contrib import admin

# Register your models here.
from .models import *

# Company Related
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

#News
class NewsImpactInline(admin.TabularInline):
    model = NewsImpact

class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImpactInline]

#Parameters
class ParameterAdmin(admin.ModelAdmin):
	model = Parameter

admin.site.register(Company, CompanyAdmin)

admin.site.register(News, NewsAdmin)

admin.site.register(Loan)

admin.site.register(Parameter, ParameterAdmin)
