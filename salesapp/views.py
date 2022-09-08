from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from salesapp.models import SalesAgent, SalesReport
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from salesapp.serializer import SalesAgentSerializer, SalesReportSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics


class HomePageView(View):
    """Display Homepage"""

    def get(self, request):
        return render(request, "home.html")


class SalesAgentsGenerics(generics.ListCreateAPIView):
    queryset = SalesAgent.objects.all().values()
    serializer_class = SalesAgentSerializer
    renderer_classes = [TemplateHTMLRenderer]
    
    style = {"template_pack": "rest_framework/vertical/"}

    def list(self, request, pk=None):
        queryset = SalesAgent.objects.all().values()
        serializer = SalesAgentSerializer(queryset, many=True)
        return Response({"sales_agents":serializer.data}, template_name="sales_agent_list.html")

    # def get(self, request):
    #     serializer = SalesAgentSerializer()
    #     return Response({"serializer": serializer, "style": self.style})

    def post(self, request, pk, *args, **kwargs):
        myobj = get_object_or_404(SalesAgent, pk=pk)
        serializer = self.get_serializer(myobj)
        return Response({"serializer":serializer}, template_name="create_sales_agent.html")

class SalesAgentList(APIView):
    """Display a list of sales agents"""

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "sales_agent_list.html"

    def get(self, request):
        sales_agents = SalesAgent.objects.all().values()
        serializer = SalesAgentSerializer(sales_agents, many=True)
        return Response({"sales_agents": serializer.data})


class CreateSalesAgent(APIView):
    """Create an object sales agent"""

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "create_sales_agent.html"
    style = {"template_pack": "rest_framework/vertical/"}

    def get(self, request):
        serializer = SalesAgentSerializer()
        return Response({"serializer": serializer, "style": self.style})

    def post(self, request):
        serializer = SalesAgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("sales_agents_list")
        return Response({"serializer": serializer, "style": self.style})


class CreateSalesReport(APIView):
    """Create sales report object of a particlular sales agent"""

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "create_sales_report.html"
    style = {"template_pack": "rest_framework/vertical/"}

    def get(self, request, id):
        serializer = SalesReportSerializer()
        return Response({"serializer": serializer, "style": self.style})

    def post(self, request, id):
        sales_agent = get_object_or_404(SalesAgent, id=id)
        serializer = SalesReportSerializer(data=request.data)
        if serializer.is_valid():
            SalesReport.objects.create(
                sales_agent=sales_agent,
                period=serializer.data.get("period"),
                sales_volume=serializer.data.get("sales_volume"),
            )
            return redirect(
                reverse_lazy("sales_reports_list_agent_api", kwargs={"id": id})
            )
        return Response({"serializer": serializer, "style": self.style})


class AgentSalesReport(APIView):
    """Display a list of sales reports of a particular agent"""

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "sales_report_list_agent.html"

    def get(self, request, id):
        sales_agent = get_object_or_404(SalesAgent, id=id)
        sales_reports = SalesReport.objects.filter(sales_agent__id=sales_agent.id)
        serializer = SalesReportSerializer(sales_reports, many=True)
        return Response(
            {"sales_agent_name": sales_agent.name, "sales_reports": serializer.data}
        )


class SalesReportsList(APIView):
    """Display a list of all sales reports"""

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "sales_report_list.html"

    def get(self, request):
        sales_reports = SalesReport.objects.all()
        serializer = SalesReportSerializer(sales_reports, many=True)
        return Response({"sales_reports": serializer.data})
