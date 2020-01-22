# from django.urls import path
# from .views import (CropStockHomeView,
#                     crop_stock_create_view,
#                     crop_stocks_list_view,
#                     crop_stock_detail_view,
#                     crop_stock_update_view, )

# app_name = 'sample_results'
# urlpatterns = [
#     path('', CropStockHomeView.as_view(), name="sample_request_home"),
#     path('add-result/', crop_stock_create_view, name="sample_request_create"),
#     path('sample-results/', crop_stocks_list_view, name="sample_requests_list"),
#     path('<int:pk>/details', crop_stock_detail_view, name="sample_request_details"),
#     path('<int:pk>/update', crop_stock_update_view, name="sample_request_update"),
#     # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
# ]