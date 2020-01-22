from django.conf import settings
from django.db import models

# Create your models here.
from farm_contracts.models import FarmContractModel
from crop_distance_charges.models import CropDistanceChargeModel


class CropTransportContractModel(models.Model):
    farm_contract = models.ForeignKey(FarmContractModel, null=True, blank=True, on_delete=models.SET_NULL,
                                      verbose_name="Crop's Farm Contract")
    agv_crop_trans_rate = models.ForeignKey(CropDistanceChargeModel, blank=True, null=True,
                                            on_delete=models.SET_NULL, related_name="crop_trans_rate",
                                            verbose_name="Crop Distance Charge Rate")
    cust_rate_km_ton = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                           verbose_name="Customer's Distance Rate/KM/Ton")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="crop_trans_contract_creator")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="crop_trans_contract_updater")