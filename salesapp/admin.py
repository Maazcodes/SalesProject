from django.contrib import admin
from salesapp.models import SalesAgent, SalesReport
# Register your models here.

admin.site.register(SalesReport)
admin.site.register(SalesAgent)
