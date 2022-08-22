from django.urls import path
from salesapp import views

urlpatterns = [
    path("home/", views.HomePageView.as_view(), name="home" ),
    # rest frame work
    path("agents/", views.SalesAgentList.as_view(), name="sales_agents_list"),
    path("reports/", views.SalesReportsList.as_view(), name="sales_reports_list"),
    path("create-agent/", views.CreateSalesAgent.as_view(), name="create_sales_agent"),
    path("create-report-api/<int:id>/", views.CreateSalesReport.as_view(), name="create_sales_report_api"),
    path("report-agent-api/<int:id>/", views.AgentSalesReport.as_view(), name="sales_reports_list_agent_api"),
]