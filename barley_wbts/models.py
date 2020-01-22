# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.
from django.conf import settings

from farms.models import FarmModel
from barley_loading_orders.models import BarleyLoadingOrderModel


class BarleyFarmWBTTruckModel(models.Model):
    wbt_no = models.IntegerField(decimal_places=4, max_digits=20, default=0.00, verbose_name="Weigh Bridge Number")
    barley_loading_order = models.ForeignKey(BarleyLoadingOrderModel, null=True, blank=True,
                                             on_delete=models.SET_NULL, verbose_name="Barley Loading Order")
    truck_reg_number = models.CharField(max_length=254, blank=True, default="", verbose_name="Crop Code")
    truck_1_weight = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                         verbose_name="Truck First Weight")
    truck_2_weight = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                         verbose_name="Truck Second Weight")
    quantity_kgs = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                       verbose_name="Loaded Quantity in KGs:")
    quantity_tons = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                        verbose_name="Loaded Quantity in Tonnes")
    delivery_note_number = models.IntegerField(decimal_places=4, max_digits=20, default=0.00, 
                                               verbose_name="Weigh Bridge Number")
    # delivery_note_scan = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
    #                                        verbose_name="Delivery Note Scan")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Farm WBT")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="barley_wbt_creator", )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="barley_wbt_update", )