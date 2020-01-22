from django.db import models
from django.urls import reverse

# Create your models here.
from farms.models import FarmModel
from sample_requests.models import SampleRequestModel
from django.conf import settings


class BarleySampleResultModel(models.Model):
    sample_request = models.OneToOneField(SampleRequestModel, blank=True, null=True, related_name='barley_result',
                                          on_delete=models.SET_NULL, verbose_name="Barley Sample Requested")
    moisture = models.CharField(max_length=254, blank=True, default="", verbose_name="Moisture Content")
    nitrogen = models.CharField(max_length=254, blank=True, default="", verbose_name="Nitrogen Content")
    rubbish = models.CharField(max_length=254, blank=True, default="", verbose_name="Rubbish Content")
    grain_size = models.CharField(max_length=254, blank=True, default="", verbose_name="Grain Size")
    extract = models.CharField(max_length=254, blank=True, default="", verbose_name="Extract")
    vita_scope = models.CharField(max_length=254, blank=True, default="", verbose_name="Vita Scope")
    extract = models.CharField(max_length=254, blank=True, default="", verbose_name="Extract")
    g_c = models.CharField(max_length=254, blank=True, default="", verbose_name="G_C")
    w_s = models.CharField(max_length=254, blank=True, default="", verbose_name="W_S")
    g_e = models.CharField(max_length=254, blank=True, default="", verbose_name="G_E")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="barley_result_creator", )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="barley_result_k_update", )

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("crop_stocks:crop_stock_details", kwargs={"pk": self.id})


class WheatSampleResultModel(models.Model):
    sample_request = models.OneToOneField(SampleRequestModel, blank=True, null=True, related_name='wheat_result',
                                          on_delete=models.SET_NULL, verbose_name="Wheat Sample Requested", )
    bushel = models.CharField(max_length=254, blank=True, default="", verbose_name="Bushel Content")
    moisture = models.CharField(max_length=254, blank=True, default="", verbose_name="Moisture Content")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="wheat_result_creator", )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="wheat_result_update", )

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("crop_stocks:crop_stock_details", kwargs={"pk": self.id})


class PulsesSampleResultModel(models.Model):
    sample_request = models.OneToOneField(SampleRequestModel, blank=True, null=True, related_name='pulse_result',
                                          on_delete=models.SET_NULL, verbose_name="Pulses Sample Requested")
    color = models.CharField(max_length=254, blank=True, default="", verbose_name="Grain Color")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="pulse_creator", )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="pulse_updater", )

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("crop_stocks:crop_stock_details", kwargs={"pk": self.id})