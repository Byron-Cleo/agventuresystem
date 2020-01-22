import os
import random

from django.conf import settings
from django.urls import reverse
from django.db import models

# Create your models here.
from transporters.models import TransportModel


# def get_filename_ext(filepath):
#     base_name = os.path.basename(filepath)
#     name, ext = os.path.splitext(base_name)
#     return name, ext


# def upload_image_path(instance, filename):
#     # print(instance)
#     # print(filename)
#     new_filename = random.randint(1, 3910209312)
#     name, ext = get_filename_ext(filename)
#     final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
#     return "drivers/{new_filename}/{final_filename}".format(
#         new_filename=new_filename,
#         final_filename=final_filename
#     )


class DriverModel(models.Model):
    full_name = models.CharField(max_length=254, default="", verbose_name="Full Name:")
    # transporter = models.ForeignKey(TransportModel, blank=True, null=True, on_delete=models.SET_NULL,
    #                                 related_name="drivers", verbose_name="Belongs to Transporter:")
    id_number = models.IntegerField(default="")
    mobile_number = models.CharField(max_length=254, default="", verbose_name="Mobile Number:")
    licence_number = models.CharField(max_length=254, default="", verbose_name="Driver Licence:")
    # driver_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
    #                                  verbose_name="Driver Photo:")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="driver_creator")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="driver_updater")

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("drivers:driver_details", kwargs={"pk": self.id})
