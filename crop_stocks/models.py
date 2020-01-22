from django.db import models
from django.urls import reverse

# Create your models here.
from django.conf import settings

from farms.models import FarmModel


class CropStockModel(models.Model):
    CROP_SALE_STATUS = (
        ("", "Specify iF For Sale or Not for Sale"),
        ("sale", "For Sale"),
        ("nosale", "Not For Sale"),
    )
    name = models.CharField(max_length=254, blank=True, default="", verbose_name="Crop Name")
    code = models.CharField(max_length=254, blank=True, default="", verbose_name="Crop Code")
    variety = models.CharField(max_length=254, blank=True, default="", verbose_name=" Crop Variety")
    grade = models.CharField(max_length=254, blank=True, default="", verbose_name="Crop Grade")
    comment = models.CharField(max_length=254, blank=True, default="", verbose_name="Comment")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Farm From")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="crop_stock_creator", )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="crop_stock_update", )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("crop_stocks:crop_stock_details", kwargs={"pk": self.id})