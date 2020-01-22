from django.db import models
from django.urls import reverse

# Create your models here.
from django.conf import settings

from barley_trans_contracts.models import BarleyTransportContractModel
from farms.models import FarmModel
from transportes.models import TransportModel
from drivers.models import DriverModel
from trucks.models import TruckModel
from trailers.models import TrailerModel


class BarleyLoadingOrderModel(models.Model):
    barley_trans_contract = models.ForeignKey(BarleyTransportContractModel, blank=True, null=True,
                                              on_delete=models.SET_NULL, related_name="barley_cont", )
    max_loading_weight = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                             verbose_name="Total Max. Loading Order Quantity (KGs)")
    transporter = models.ForeignKey(TransportModel, blank=True, null=True, on_delete=models.SET_NULL,
                                    related_name="barley_transporters", verbose_name="Transporter")
    driver = models.ForeignKey(DriverModel, blank=True, null=True, on_delete=models.SET_NULL,
                               related_name="barley_drivers", verbose_name="Driver(s):")
    truck = models.ForeignKey(TruckModel, blank=True, null=True, on_delete=models.SET_NULL,
                              related_name="barley_trucks", verbose_name="Truck(s):")
    trailer = models.ForeignKey(TrailerModel, blank=True, null=True, on_delete=models.SET_NULL,
                                related_name="barley_trailers", verbose_name="Trailer(s):")
    description = models.TextField(max_length=254, blank=True, default="", verbose_name="Describe Weight per Truck")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Farm From")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="barley_loading_creator", )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="barley_loading_update", )

    # def __str__(self):
    #     return self.name
    #
    # def get_absolute_url(self):
    #     return reverse("crop_stocks:crop_stock_details", kwargs={"pk": self.id})