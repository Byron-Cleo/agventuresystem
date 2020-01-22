from django.urls import path
from .views import (CustomerHomeView,
                    customer_create_view,
                    customers_list_view,
                    customer_detail_view,
                    customer_update_view, )


app_name = 'customers'
urlpatterns = [
    path('', CustomerHomeView.as_view(), name="customers_home"),
    path('create/', customer_create_view, name="customer_create"),
    path('agv-customers/', customers_list_view, name="customers_list"),
    path('<int:pk>/details', customer_detail_view, name="customer_details"),
    path('<int:pk>/update', customer_update_view, name="customer_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]


