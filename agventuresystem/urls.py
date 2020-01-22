"""agventuresystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import (AgvHomeView, UserManagementView, SampleQualityView,
                    SalesPlatformView, TransportLogisticsView,
                    FarmsPlatformView, AccountingPlatformView, )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AgvHomeView.as_view(), name="agv_home"),
    path('user-management/', UserManagementView.as_view(), name='user_management'),
    path('sample-quality/', SampleQualityView.as_view(), name='sample_quality'),
    path('sales-platform/', SalesPlatformView.as_view(), name='sales_platform'),
    path('transport-logistics/', TransportLogisticsView.as_view(), name='transport_logistic'),
    path('farms-platform/', FarmsPlatformView.as_view(), name='farms_platform'),
    path('agv-accounting-platform/', AccountingPlatformView.as_view(), name='accounting_platform'),
    path('farms/', include('farms.urls', namespace='farms')),
    path('crop-stocks/', include('crop_stocks.urls', namespace='crop_stocks')),
    path('customers/', include('customers.urls', namespace='customers')),
    path('sample-requests/', include('sample_requests.urls', namespace='sample_requests')),
    # path('sample-results/', include('sample_results.urls', namespace='sample_results')),
    path('customer-interests/', include('customer_interests.urls', namespace='customer_interests')),
    path('customer-contracts/', include('customer_contracts.urls', namespace='customer_contracts')),
    path('farm-contracts/', include('farm_contracts.urls', namespace='farm_contracts')),
    path('payments/', include('customer_payments.urls', namespace='customer_payments')),
    path('transporters/', include('transporters.urls', namespace='transporters')),
    path('drivers/', include('drivers.urls', namespace='drivers')),
    path('trucks/', include('trucks.urls', namespace='trucks')),
    path('trailers/', include('trailers.urls', namespace='trailers')),

]
