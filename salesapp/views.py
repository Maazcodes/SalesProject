from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from salesapp.models import SalesAgent, SalesReport
from salesapp.forms import SalesAgentForm, SalesReportForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

class HomePageView(View):
    def get(self, request):
        return render(request, "home.html")

class SalesAgentList(ListView):
    model = SalesAgent
    context_object_name = 'sales_agents'
    template_name = "sales_agent_list.html"

class CreateSalesAgent(SuccessMessageMixin, CreateView):
    model = SalesAgent
    template_name = "create_sales_agent.html"
    success_message = 'Sales agent record successfully created!'
    success_url = reverse_lazy("sales_agents_list")
    form_class = SalesAgentForm

class SalesReportsList(ListView):

    """ View all reports"""
    model = SalesReport
    context_object_name = 'sales_reports'
    template_name = "sales_report_list.html"

class SalesReportsListOfSalesAgent(ListView):
    """ View reports of a specific sales agent"""
    model = SalesReport
    context_object_name = 'sales_reports'
    template_name = "sales_report_list_agent.html"

    def get_object(self):
        sales_agent_id = self.kwargs.get("id")
        return get_object_or_404(SalesAgent, id=sales_agent_id)
    
    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)                     
        sales_agent = self.get_object()
        context["sales_agent_name"] = sales_agent.name
        return context

    def get_queryset(self):
        sales_agent_id = self.get_object().id
        return self.model.objects.filter(sales_agent__id = sales_agent_id)

class CreateSalesReport(SuccessMessageMixin, CreateView):
    model = SalesReport
    template_name = "create_sales_report.html"
    success_message = 'Sales Report successfully created!'
    form_class = SalesReportForm

    def get_object(self):
        sales_agent_id = self.kwargs.get("id")
        return get_object_or_404(SalesAgent, id=sales_agent_id)

    def form_valid(self, form):
        form.instance.sales_agent = self.get_object()
        form.save()
        return super(CreateSalesReport, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy("sales_reports_list_agent", kwargs={'id': self.get_object().id})