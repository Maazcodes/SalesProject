from django import forms
from salesapp.models import SalesAgent, SalesReport
from djmoney.forms.widgets import MoneyWidget
from salesproject import settings

class SalesAgentForm(forms.ModelForm):

    class Meta:
        model = SalesAgent
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["hire_date"].widget = DateInput()
        self.fields["birthday"].widget = DateInput()


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class SalesReportForm(forms.ModelForm):
    
    class Meta:
        model = SalesReport
        fields = ['period', 'sales_volume']
        widgets = {
        'sales_volume': MoneyWidget(
            amount_widget=forms.TextInput(attrs={'class':'form-class'}),
            currency_widget=forms.Select(attrs={
                },
                choices= settings.CURRENCY_CHOICES,
            ),
        ),
        # ... Here more widget fields
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["period"].widget = DateInput()
