from django.conf import settings
from django.urls import reverse
from django.db import models

# Create your models here.
# from addresses.models import Address


class TransportModel(models.Model):
    CONTRACT_STATUS = (
        ("", "Specify if the Transporter is Still Working with Agventure Ltd"),
        ("active", "Active"),
        ("not active", "Not Active"),
    )

    name = models.CharField(max_length=254, blank=True, default="", verbose_name="Transporter Name")
    # address = models.OneToOneField(Address, blank=True, null=True, on_delete=models.SET_NULL,
    #                                related_name="transporters", verbose_name="Transporter Address")
    contract_status = models.CharField(max_length=254, choices=CONTRACT_STATUS, default="",
                                       verbose_name="AGV-Transporter Contract Status")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="transporter_creator")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="transporter_updater")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("transporters:transporter_details", kwargs={"pk": self.id})