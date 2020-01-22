from django.db import models
from django.urls import reverse

# Create your models here.
from django.conf import settings

from crops_trans_contracts.models import CropTransportContractModel
from farms.models import FarmModel
from transportes.models import TransportModel
from drivers.models import DriverModel
from trucks.models import TruckModel
from trailers.models import TrailerModel


class CropLoadingOrderModel(models.Model):
    crops_trans_contract = models.ForeignKey(CropTransportContractModel, blank=True, null=True,
                                             on_delete=models.SET_NULL, related_name="crop_cont", )
    max_loading_weight = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                             verbose_name="Crop Max. Loading Order Quantity (KGs)")
    transporter = models.ForeignKey(TransportModel, blank=True, null=True, on_delete=models.SET_NULL,
                                    related_name="crop_transporters", verbose_name="Transporter")
    driver = models.ForeignKey(DriverModel, blank=True, null=True, on_delete=models.SET_NULL,
                               related_name="crop_drivers", verbose_name="Driver(s):")
    truck = models.ForeignKey(TruckModel, blank=True, null=True, on_delete=models.SET_NULL,
                              related_name="crop_trucks", verbose_name="Truck(s):")
    trailer = models.ForeignKey(TrailerModel, blank=True, null=True, on_delete=models.SET_NULL,
                                related_name="crop_trailers", verbose_name="Trailer(s):")
    description = models.TextField(max_length=254, blank=True, default="", verbose_name="Describe Weight per Truck")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Farm From")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="crop_loading_creator", )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="crop_loading_update", )