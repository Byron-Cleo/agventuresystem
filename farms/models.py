from django.conf import settings
from django.urls import reverse

from django.db import models


# Create your models here.
class FarmModel(models.Model):
    name = models.CharField(max_length=254, blank=True, default="", verbose_name="Farm Name")
    short_name = models.CharField(max_length=254, blank=True, default="", verbose_name="Farm Abbv.")
    mobile = models.CharField(max_length=254, blank=True, default="", verbose_name="Farm Telephone No.")
    email = models.EmailField(max_length=254, blank=True, default="", verbose_name="Farm Email")
    region = models.CharField(max_length=254, blank=True, default="", verbose_name="Farm Region")
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="farm_create")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="farm_update")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("farms:farm_details", kwargs={"slug": self.slug})
        return reverse("farms:farm_details", kwargs={"pk": self.id})