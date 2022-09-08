from django.urls import path
from salesapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("home/", views.HomePageView.as_view(), name="home" ),
    # rest frame work
    path(r'^agents-generic/(?P<pk>[0-9]+)/$', views.SalesAgentsGenerics.as_view(), name="agents-generic"),
    path("agents/", views.SalesAgentList.as_view(), name="sales_agents_list"),
    path("reports/", views.SalesReportsList.as_view(), name="sales_reports_list"),
    path("create-agent/", views.CreateSalesAgent.as_view(), name="create_sales_agent"),
    path("create-report-api/<int:id>/", views.CreateSalesReport.as_view(), name="create_sales_report_api"),
    path("report-agent-api/<int:id>/", views.AgentSalesReport.as_view(), name="sales_reports_list_agent_api"),
]

urlpatterns+=staticfiles_urlpatterns()
