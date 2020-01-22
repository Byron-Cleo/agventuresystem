from django.urls import path
from .views import (CustomerPaymentHomeView,
                    customer_pay_create_view,
                    customer_pay_list_view,
                    customer_pay_detail_view,
                    customer_pay_update_view,)

app_name = 'customer_payments'
urlpatterns = [
    path('', CustomerPaymentHomeView.as_view(), name="customer_payment_home"),
    path('add-payment/', customer_pay_create_view, name="customer_payment_create"),
    path('all-customer-payments/', customer_pay_list_view, name="customer_payments_list"),
    path('<int:pk>/details', customer_pay_detail_view, name="customer_payment_details"),
    path('<int:pk>/update', customer_pay_update_view, name="customer_payment_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]


