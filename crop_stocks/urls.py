from django.urls import path
from .views import (CropStockHomeView,
                    crop_stock_create_view,
                    crop_stocks_list_view,
                    crop_stock_detail_view,
                    crop_stock_update_view, )

app_name = 'crop_stocks'
urlpatterns = [
    path('', CropStockHomeView.as_view(), name="crop_stock_home"),
    path('create/', crop_stock_create_view, name="crop_stock_create"),
    path('farm-crops-stock/', crop_stocks_list_view, name="crops_stock_list"),
    path('<int:pk>/details', crop_stock_detail_view, name="crop_stock_details"),
    path('<int:pk>/update', crop_stock_update_view, name="crop_stock_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]


