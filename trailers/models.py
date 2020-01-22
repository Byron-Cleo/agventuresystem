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
#     return "trailers/{new_filename}/{final_filename}".format(
#         new_filename=new_filename,
#         final_filename=final_filename
#     )


class TrailerModel(models.Model):
    transporter = models.ForeignKey(TransportModel, blank=True, null=True, on_delete=models.SET_NULL,
                                    related_name="trailers", verbose_name="Trailer Transporter")
    reg_number = models.CharField(max_length=254, default="Trailer Reg. Number")
    chassis_number = models.CharField(max_length=254, default="", verbose_name="Trailer Chassis Number")
    color = models.CharField(max_length=254, default="", verbose_name="Trailer Color")
    # logbook_scan_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
    #                                        verbose_name="Trailer LogBook Scann")
    # trailer_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
    #                                   verbose_name="Trailer Photo")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="trailer_creator")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="trailer_updater")

    def __str__(self):
        return self.transporter

    def get_absolute_url(self):
        return reverse("trailers:trailer_details", kwargs={"pk": self.id})