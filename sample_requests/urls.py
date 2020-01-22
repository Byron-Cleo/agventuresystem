from django.urls import path
from .views import (SampleRequestsHomeView,
                    sample_requests_list_view,
                    sample_request_create_view,
                    sample_request_detail_view,
                    sample_request_update_view, )

app_name = 'sample_requests'
urlpatterns = [
    path('', SampleRequestsHomeView.as_view(), name="sample_requests_home"),
    path('make-request/', sample_request_create_view, name="sample_request_create"),
    path('all-sample-requests/', sample_requests_list_view, name="sample_requests_list"),
    path('<int:pk>/details', sample_request_detail_view, name="sample_request_details"),
    path('<int:pk>/update', sample_request_update_view, name="sample_request_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]


0