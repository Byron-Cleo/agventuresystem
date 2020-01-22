from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.
class CustomerModel(models.Model):

    CUSTOMER_TYPE = (
        ("", "Specify The Customer Type"),
        ("individual", "Individual"),
        ("company", "Company"),
    )

    PAYMENT_TERMS = (
        ("", "Specify The Customer Department"),
        ("cash", "Cash"),
        ("prepaid", "Pre Paid"),
        ("30days", "Payment after 30 Days"),
        ("60days", "Payment after 60 Days"),
    )

    CUSTOMER_DEPARTMENT = (
        ("", "Specify The Customer Department"),
        ("1000", "1000 Administration"),
        ("1001", "1001 Centre of Excellence"),
        ("2000", "2000 Crop Sales"),
        ("3000", "3000 Marketing"),
        ("4000", "4000 Chemicals and Fertilizers"),
        ("5000", "5000 Timau Processing"),
        ("6000", "6000 Nakuru Processing"),
        ("7000", "7000 Green Peas"),
        ("8000", "8000 Operations-Nairobi"),
        ("8001", "8001 Pulses"),
        ("8999", "8999 Others"),
        ("9000", "9000 Operations-Nakuru"),
        ("9999", "9999 Seed-Business"),
    )

    CURRENCY = (
        ("", "Specify Currency of Trade"),
        ("ksh", "KSH"),
        ("usd", "USD"),
    )

    CUSTOMER_CATEGORY = (
        ("", "Specify Customer Category"), ("feeds", "Animal Feeds"), ("usd", "USD"), ("usd", "USD"), ("usd", "USD"),
        ("usd", "USD"), ("usd", "USD"), ("usd", "USD"), ("usd", "USD"), ("usd", "USD"), ("usd", "USD"), ("usd", "USD"),
        ("usd", "USD"), ("usd", "USD"), ("usd", "USD"), ("usd", "USD"), ("usd", "USD"), ("usd", "USD"),
    )

    name = models.CharField(max_length=254, default="", verbose_name="Customer Name")
    type = models.CharField(max_length=254, choices=CUSTOMER_TYPE, blank=True, default="",
                            verbose_name="Customer Type")
    category = models.CharField(max_length=254, choices=CUSTOMER_CATEGORY, blank=True, default="",
                                verbose_name="Customer Category")
    department = models.CharField(max_length=254, choices=CUSTOMER_DEPARTMENT, default="1",
                                  verbose_name="Customer Department")
    payment_terms = models.CharField(max_length=254, choices=PAYMENT_TERMS, blank=True, default="",
                                     verbose_name="Payment Terms")
    currency = models.CharField(max_length=254, choices=CURRENCY, blank=True, default="",
                                verbose_name="Currency")
    reg_no = models.CharField(max_length=254, blank=True, default="", verbose_name="Customer Reg. Number", )
    vat_reg = models.CharField(max_length=254, blank=True, default="", verbose_name="Customer VAT Reg.", )
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="customer_creator", )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="customer_updater", )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customers:customer_details", kwargs={"pk": self.id})