from django.views.generic import TemplateView
from django.shortcuts import render, redirect

class AgvHomeView(TemplateView):
    template_name = "agv-home.html"


class UserManagementView(TemplateView):
    template_name = "user-management-platform.html"


class SampleQualityView(TemplateView):
    template_name = "sample-quality.html"


class SalesPlatformView(TemplateView):
    template_name = "sales-platform.html"


class TransportLogisticsView(TemplateView):
    template_name = "transport-logistics.html"


class FarmsPlatformView(TemplateView):
    template_name = "farms-platform.html"


class AccountingPlatformView(TemplateView):
    template_name = "accounting-platform.html"