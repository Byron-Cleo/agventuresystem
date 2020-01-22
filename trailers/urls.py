from django.urls import path
from .views import (TrailerHomeView,
                    trailer_list_view,
                    trailer_create_view,
                    trailer_detail_view,
                    trailer_update_view,
                    )

app_name = 'trailers'
urlpatterns = [
    path('', TrailerHomeView.as_view(), name="trailers_home"),
    path('add-new-trailer/', trailer_create_view, name="trailer_create"),
    path('all-transporters/', trailer_list_view, name="trailer_list"),
    path('<int:pk>/details', trailer_detail_view, name="trailer_details"),
    path('<int:pk>/update', trailer_update_view, name="trailer_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]


