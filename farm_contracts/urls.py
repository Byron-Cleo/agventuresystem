from django.urls import path
from .views import (FarmContractHomeView,
                    farm_contract_create_view,
                    farm_contracts_list_view,
                    farm_contract_detail_view,
                    farm_contract_update_view,
                    )

app_name = 'farm_contracts'
urlpatterns = [
    path('', FarmContractHomeView.as_view(), name="farm_contact_home"),
    path('gen-contract/', farm_contract_create_view, name="farm_contract_create"),
    path('all-farm-contracts/', farm_contracts_list_view, name="farm_contracts_list"),
    path('<int:pk>/details', farm_contract_detail_view, name="farm_contract_details"),
    path('<int:pk>/update', farm_contract_update_view, name="farm_contract_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]


