from django.db import models
from django.urls import reverse
from django.conf import settings

# from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your models here.
from crop_stocks.models import CropStockModel
from customers.models import CustomerModel
from farms.models import FarmModel


class CustomerInterestModel(models.Model):
    ORDER_TYPE = (
        ("", "Specify Supply Order in Bulk/Bags"),
        ("bulk", "Bulk Order"),
        ("bags", "Bags Order"),
    )

    FARM_APPROVAL = (
        ("", "Please Approve/Disapprove the Cust. Order"),
        ("approved", "Order Approved"),
        ("not approved", "Order Not Approved"),
    )

    PAYMENT_TERMS = (
        ("", "Specify Customer Payment Terms "),
        ("cash", "Cash"),
        ("prepaid", "Pre-Paid"),
        ("30days", "Payment after 30 Days"),
        ("60days", "Payment after 60 Days"),
    )

    BAG_TYPE = (
        ("", "Specify Interested Bag Type"),
        ("90", "90 KG"),
        ("50", "50 KG"),
    )

    customer = models.ForeignKey(CustomerModel, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="customer_orders", verbose_name="Customer Name")
    crop_name = models.ForeignKey(CropStockModel, blank=True, null=True, on_delete=models.SET_NULL,
                                  related_name="customer_interests", verbose_name="Crop of Interest/Order")
    order_type = models.CharField(max_length=254, choices=ORDER_TYPE, default="",
                                  verbose_name="Order Type")#important column here
    bag_type = models.CharField(max_length=254, choices=BAG_TYPE, default=1, verbose_name="Customer Bag Type")
    ordered_quantity = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                           verbose_name="Max. Ordered Quantity (KGs)")#important column here
    cust_kg_price = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                        verbose_name="Customer Price/KG (KSh)")
    farm_kg_price = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                        verbose_name="Farm Price/KG (Ksh)")
    cust_bag_price = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                         verbose_name="Customer Bag/KG (KSh)")#calculated field
    farm_bag_price = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                         verbose_name="Farm Price/Bag (Ksh)") #calculated field & Price to be approved by the farmer
    total_bags = models.DecimalField(decimal_places=4, max_digits=20, default=0.00, verbose_name="Total Bags")
    farm_approval = models.CharField(max_length=254, choices=FARM_APPROVAL, default="", verbose_name="Farm App/Disapp.")
    payment_terms = models.CharField(max_length=254, choices=PAYMENT_TERMS, default="", verbose_name="Payment Terms")
    cust_dest = models.CharField(max_length=254, default="", verbose_name="Customer Destination")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="interest_creator")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="interest_updater")

    def __str__(self):
        return self.customer

    def get_absolute_url(self):
        return reverse("customer_interests:customer_interest_details", kwargs={"pk": self.id})


