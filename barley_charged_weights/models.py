from django.db import models

# Create your models here.
from django.urls import reverse

# Create your models here.
from django.conf import settings

from farms.models import FarmModel
from barley_wbt.models import BarleyFarmWBTTruckModel


class BarleyChargedWeightModel(models.Model):
    barley_farm_wbt = models.ForeignKey(BarleyFarmWBTTruckModel, null=True, blank=True,
                                        on_delete=models.SET_NULL, verbose_name="Crop Loading Order")
    customer_venue = models.CharField(max_length=254, blank=True, default="",
                                      verbose_name="Customer Venue of Weight Reading")
    customer_weight_reading = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                                  verbose_name="Customer's Barley Weight Reading")
    first_party_venue = models.CharField(max_length=254, blank=True, default="",
                                         verbose_name="1st Party Venue of Weight Reading")
    first_party_weight_reading = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                                     verbose_name="1st Party Weight Reading (KGs")
    second_party_venue = models.CharField(max_length=254, blank=True, default="",
                                          verbose_name="2nd Party Venue of Weight Reading")
    second_party_weight_reading = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                                      verbose_name="2nd Party Weight Reading (KGs)")
    barley_agreed_charged_weight = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                                       verbose_name="Barley Agreed Truck Charged Weight")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Farm WBT")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="barley_charged_weight_creator", )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="barley_charged_weight_update", )

    # def __str__(self):
    #     return self.name
    #
    # def get_absolute_url(self):
    #     return reverse("crop_stocks:crop_stock_details", kwargs={"pk": self.id})