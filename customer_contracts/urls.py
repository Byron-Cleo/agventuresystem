from django.urls import path
from .views import (CustomerContractHomeView,
                    customer_contract_create_view,
                    customer_contracts_list_view,
                    customer_contract_detail_view,
                    customer_contract_update_view,
                    )

app_name = 'customer_contracts'
urlpatterns = [
    path('', CustomerContractHomeView.as_view(), name="home_customer_contact"),
    path('gen-contract/', customer_contract_create_view, name="customer_contract_create"),
    path('all-customer-contracts/', customer_contracts_list_view, name="customer_contracts_list"),
    path('<int:pk>/details', customer_contract_detail_view, name="customer_contract_details"),
    path('<int:pk>/update', customer_contract_update_view, name="customer_contract_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]


