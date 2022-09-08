from django.db import models
# Create your models here.

class SalesAgent(models.Model):
    name = models.CharField(max_length=100)
    hire_date = models.DateField("Hire Date")
    birthday = models.DateField("Birthday")
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class SalesReport(models.Model):
    sales_agent = models.ForeignKey(SalesAgent, on_delete=models.CASCADE, related_name="reports")
    period = models.DateField("Period")
    sales_volume = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sales Volume in EUR")

    def __str__(self):
        return f"Report of {self.sales_agent.name}"

    def sales_agent_name(self):
        return self.sales_agent.name
