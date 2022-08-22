from tabnanny import verbose
from rest_framework import serializers
from salesapp.models import SalesAgent,SalesReport
from django import template
import calendar

    

class SalesAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesAgent
        fields = '__all__'
        
class SalesReportSerializer(serializers.Serializer):
    sales_agent = serializers.ReadOnlyField(source='sales_agent.name')
    period = serializers.DateField()
    sales_volume = serializers.DecimalField(max_digits=10, decimal_places=2)

