from django.db import models
from django.urls import reverse

# Create your models here.
from django.conf import settings
from django.db import models

# Create your models here.
from customer_contracts.models import CustomerContractModel
from farms.models import FarmModel


class FarmContractModel(models.Model):
    BAG_TYPE = (
        ("", "Specify Interested Bag Type"),
        ("1", "90 KG"),
        ("2", "50 KG"),
    )

    BULK_BAG = (
        ("", "Specify Interested Bag Type"),
        ("1", "90 KG"),
        ("2", "50 KG"),
    )

    buyer = models.CharField(max_length=254, default="Agventure Ltd.", verbose_name="Agventure Ltd. (Buyer)")
    farm_contract_code = models.CharField(max_length=254, default="xyBMAr2019",
                                          verbose_name="Farm Contract Code")#1912B108 = Year  Month  Cropabv  AutoNumber
    customer_contract = models.ForeignKey(CustomerContractModel, null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name="farm_contracts", verbose_name="Customer Contract FK")
    ordered_quantity = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                           verbose_name="Ordered Quantity (KGs)")
    bag_type = models.CharField(max_length=254, choices=BAG_TYPE, default="1", verbose_name="Bag Type")
    bulk_bags = models.CharField(max_length=254, choices=BULK_BAG, default="1", verbose_name="Bulk or Bags Order Type")
    total_bags = models.DecimalField(decimal_places=4, max_digits=20, default=0.00, verbose_name="No. of Bags")
    farm_kg_price = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                        verbose_name="Farm Price/KG (KSH)")
    farm_bag_price = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                         verbose_name="Farm Price/Bag (KSH)")
    total_farm_amount = models.DecimalField(decimal_places=4, max_digits=20, default=0.00, verbose_name="Farm Selling Price")
    farm_tolerance = models.DecimalField(decimal_places=4, max_digits=20, default=0.00, verbose_name="Tolerance +/-")
    collection_weight_bridge = models.CharField(max_length=254, blank=True, default="",
                                                verbose_name="Farm of Collection Weigh Bridge")
    delivery_weigh_bridge = models.CharField(max_length=254, blank=True, default="",
                                             verbose_name="Crop Delivery Destination (Cust. Point)")
    delivery_period = models.CharField(max_length=254, default="Delivery Period",
                                       verbose_name="Delivery Period")
    quality_specs = models.CharField(max_length=254, default="As per Sample Results",
                                     verbose_name="Crop Quality Specifications")
    offloading_fees = models.TextField(blank=True, default="No Offloading Fees for Vehicles are "
                                                           "to be Levied by the Buyer",
                                       verbose_name="Offloading Fees")
    weighing_conditions = models.TextField(blank=True, default="", verbose_name="Weighing Conditions")
    other_conditions = models.TextField(blank=True, default="", verbose_name="Other Conditions")
    governing_terms = models.TextField(blank=True, default="Kenyan Law Shall Apply", verbose_name="Governing Terms")
    whole_agreement = models.TextField(blank=True, default="", verbose_name="Whole Agreement")
    rejection_procedure = models.TextField(blank=True, default="Rejection can take place at the Farm. Once Accepted"
                                                               " and Carried, no Rejection can Take Place. ",
                                           verbose_name="Rejection Procedure")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL,
                             related_name="seller_farmer", verbose_name="Farm Selling")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Contract Date")
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="farm_contract_creator")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="farm_contract_updater")

    def __str__(self):
        return self.buyer

    def get_absolute_url(self):
        return reverse("farm_contracts:farm_contract_details", kwargs={"pk": self.id})







