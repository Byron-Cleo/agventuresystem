from django.conf import settings
from django.db import models

# Create your models here.
from farms.models import FarmModel


class CropDistanceChargeModel(models.Model):
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL,
                             verbose_name="Farm of Collection")
    destination = models.CharField(max_length=254, default="", verbose_name="Customer Destination")
    distance_km = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                      verbose_name="Distance (KMs)")
    agv_rate_km_ton = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                          verbose_name="Rate/KM/Ton(KSHs)")#claculated
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="crop_charge_creator")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="crop_charge_updater")