from django.conf import settings
from django.db import models

# Create your models here.
from farm_contracts.models import FarmContractModel
from barley_transport_rates.models import BarleyDistanceRatesModel


class BarleyTransportContractModel(models.Model):
    farm_contract = models.ForeignKey(FarmContractModel, null=True, blank=True, on_delete=models.SET_NULL,
                                      verbose_name="Barley's Farm Contract")
    agv_barley_trans_rate = models.ForeignKey(BarleyDistanceRatesModel, blank=True, null=True,
                                              on_delete=models.SET_NULL, related_name="barley_trans_rate",
                                              verbose_name="Barley Transport Rate")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="barley_trans_contract_creator")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="barley_trans_contract_updater")