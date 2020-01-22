from django.conf import settings
from django.urls import reverse
from django.db import models

# Create your models here.
from farms.models import FarmModel
from customers.models import CustomerModel


class CustomerContractModel(models.Model):
    customer = models.ForeignKey(CustomerModel, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="customer_contract",
                                 verbose_name="Customer (Buyer)FK")
    seller = models.CharField(max_length=254, default="Agventure Ltd.",
                              verbose_name="Agventure Ltd. (Seller)")
    cust_contract_code = models.CharField(max_length=254, default="",
                                          verbose_name="Customer Contract Code") #1912B108 = Year  Month  Cropabv  AutoNumber
    agv_kg_price = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                       verbose_name="AGV Price/KG (KSH)") #from customer interest
    agv_bag_price = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                        verbose_name="AGV Price/Bag (KSh)") #calculated Field
    cust_tolerance = models.DecimalField(decimal_places=4, max_digits=20, default=0.00,
                                         verbose_name="Cust. Contract Tolerance +/-")
    delivery_period = models.CharField(max_length=254, default="Delivery Period",
                                       verbose_name="Delivery Period")
    quality_specs = models.CharField(max_length=254, default="",
                                     verbose_name="Crop Quality Specifications")
    delivery_terms = models.TextField(max_length=254, default="Transport Details to be supplied "
                                                              "One Day in Advance by Buyer....",
                                      verbose_name="Delivery Terms")
    offloading_fees = models.TextField(blank=True, default="No Offloading Fees for Vehicles are "
                                                           "to be Levied by the Buyer",
                                       verbose_name="Offloading Fees")
    other_conditions = models.TextField(blank=True, default="",
                                        verbose_name="Other Conditions")
    governing_terms = models.TextField(blank=True, default="Kenyan Law Shall Apply",
                                       verbose_name="Governing Terms")
    whole_agreement = models.TextField(blank=True, default="",
                                       verbose_name="Whole Agreement")
    rejection_procedure = models.TextField(blank=True, default="Rejection can take place at the Farm. Once Accepted"
                                                               " and Carried, no Rejection can Take Place. ",
                                           verbose_name="Rejection Procedure")
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL,
                             related_name="cust_contracts")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="customer_contract_creator")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="customer_contract_updater")
    # publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.seller

    def get_absolute_url(self):
        return reverse("customer_contracts:customer_contract_details", kwargs={"pk": self.id})






