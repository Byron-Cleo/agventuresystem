from django.urls import path
from .views import (TransporterHomeView,
                    transporter_create_view,
                    transporters_list_view,
                    transporter_detail_view,
                    transporter_update_view,
                    )

app_name = 'transporters'
urlpatterns = [
    path('', TransporterHomeView.as_view(), name="transporters_home"),
    path('add-new-transporter/', transporter_create_view, name="transporter_create"),
    path('all-transporters/', transporters_list_view, name="transporter_list"),
    path('<int:pk>/details', transporter_detail_view, name="transporter_details"),
    path('<int:pk>/update', transporter_update_view, name="transporter_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]


