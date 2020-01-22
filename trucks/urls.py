from django.urls import path
from .views import (TruckHomeView,
                    truck_create_view,
                    truck_list_view,
                    truck_detail_view,
                    truck_update_view,
                    )

app_name = 'trucks'
urlpatterns = [
    path('', TruckHomeView.as_view(), name="trucks_home"),
    path('add-new-truck/', truck_create_view, name="truck_create"),
    path('all-transporters/', truck_list_view, name="truck_list"),
    path('<int:pk>/details', truck_detail_view, name="truck_details"),
    path('<int:pk>/update', truck_update_view, name="truck_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]


