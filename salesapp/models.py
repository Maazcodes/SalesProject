from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.

class SalesAgent(models.Model):
    name = models.CharField(max_length=100, verbose_name="Agent Name")
    hire_date = models.DateField("Hire Date")
    birthday = models.DateField("Birthday")
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class SalesReport(models.Model):
    sales_agent = models.ForeignKey(SalesAgent, on_delete=models.CASCADE, related_name="reports")
    period = models.DateField("Period")
    sales_volume = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')

    def __str__(self):
        return f"Report of {self.sales_agent.name}"