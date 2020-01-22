from django.urls import path
from .views import (CustomerInterestHomeView,
                    customer_interest_create_view,
                    customer_interests_list_view,
                    customer_interest_detail_view,
                    customer_interest_update_view,
                    )

app_name = 'customer_interests'
urlpatterns = [
    path('', CustomerInterestHomeView.as_view(), name="home_customer_interest"),
    path('raise-customer-interest/', customer_interest_create_view, name="customer_interest_create"),
    path('all-customer-interests/', customer_interests_list_view, name="customer_interests_list"),
    path('<int:pk>/details', customer_interest_detail_view, name="customer_interest_details"),
    path('<int:pk>/update', customer_interest_update_view, name="customer_interest_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]


