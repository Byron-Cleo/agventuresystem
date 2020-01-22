from django.urls import path
from .views import (FarmHomeView,
                    farm_create_view,
                    farms_list_view,
                    farm_detail_view,
                    farm_update_view, )

app_name = 'farms'
urlpatterns = [
    path('', FarmHomeView.as_view(), name="farm_home"),
    path('create/', farm_create_view, name="farm_create"),
    path('agv-farms/', farms_list_view, name="farms_list"),
    path('<int:pk>/details', farm_detail_view, name="farm_details"),
    path('<int:pk>/update', farm_update_view, name="farm_update"),
    # path('<int:pk>/delete', farm_delete_view, name="farm_delete"),

    # path('add/', CropstockCreateViewiew.as_view(), name="crop_create"),
    # path('<slug:slug>/', CropstockDetailView.as_view(), name="crop-detail"),
]


