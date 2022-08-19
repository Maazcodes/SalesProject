from django.urls import path
from salesapp import views

urlpatterns = [
    path("home/", views.HomePageView.as_view(), name="home" ),

    #generate sales agent
    path("agents/", views.SalesAgentList.as_view(), name="sales_agents_list"),
    path("create-agent-record/", views.CreateSalesAgent.as_view(), name="create_sales_agent"),
    
    #generate sales report
    path("reports/", views.SalesReportsList.as_view(), name="sales_reports_list"),
    path("reports-agent/<int:id>", views.SalesReportsListOfSalesAgent.as_view(), name="sales_reports_list_agent"),
    path("create-report/<int:id>/", views.CreateSalesReport.as_view(), name="create_sales_report"),
]