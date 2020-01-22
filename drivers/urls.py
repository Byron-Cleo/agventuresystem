from django.urls import path
from .views import (DriverHomeView,
                    driver_create_view,
                    drivers_list_view,
                    driver_detail_view,
                    driver_update_view)

app_name = 'drivers'
urlpatterns = [
    path('', DriverHomeView.as_view(), name="drivers_home"),
    path('add-new-driver/', driver_create_view, name="driver_create"),
    path('all-drivers/', drivers_list_view, name="driver_list"),
    path('<int:pk>/details', driver_detail_view, name="driver_details"),
    path('<int:pk>/update', driver_update_view, name="driver_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]


