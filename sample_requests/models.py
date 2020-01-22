from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
from farms.models import FarmModel
from crop_stocks.models import CropStockModel


class SampleRequestModel(models.Model):
    DELIVERY_DESTINATION = (
        ("agvoffice", "AGV Ltd. Timau Head Office"),
        ("cargil", "Cargil, Nakuru"),
        ("nairobi", "EAML Labs, Nairobi"),
    )

    REQUEST_STATUS = (
        ("created", "Request Created"),
        ("pending", "Pending"),
        ("shipped", "Sample Shipped"),
        ("delivered", "Sample Delivered"),
    )
    name = models.CharField(max_length=254, blank=True, default="Return Name Sample Request")
    crop_requested = models.ForeignKey(CropStockModel, blank=True, null=True, on_delete=models.SET_NULL,
                                       related_name="sample_requests", verbose_name="Crop Requested")
    sample_quantity = models.CharField(max_length=254, blank=True, default="",
                                       verbose_name="Sample Quantity (KGs)")
    delivery_destination = models.CharField(max_length=254, choices=DELIVERY_DESTINATION, blank=True, default="",
                                            verbose_name="Delivery Destination")
    request_status = models.CharField(max_length=254, choices=REQUEST_STATUS,blank=True, default="",
                                      verbose_name="Request Status")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="sample_request_creator", )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="sample_request_updater", )

    def __str__(self):
        return self.crop_requested

    def get_absolute_url(self):
        return reverse("sample_requests:sample_request_details", kwargs={"pk": self.id})