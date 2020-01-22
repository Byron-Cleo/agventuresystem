from django.conf import settings
from django.urls import reverse
from django.db import models

# Create your models here.
from customer_interests.models import CustomerInterestModel
from farms.models import FarmModel


class CustomerPaymentModel(models.Model):
    PAYMENT_STATUS = (
        ("", "Specify Customer Order if Paid or Not Paid"),
        ("1", "Order Paid (Confirmed)"),
        ("2", "Order Not Paid"),
    )

    BANK_PAID = (
        ("", "Specify Bank of Customer Payment"),
        ("1", "NCBA Bank - Acc. 6680660011"),
        ("2", "Victoria Commercial Bank - Acc. 1008260016"),
    )

    PAYMENT_TERMS = (
        ("", "Specify Customer Order if Paid or Not Paid"),
        ("1", "Cash"),
        ("2", "Pre-Paid"),
        ("3", "Payment after 30 Days"),
        ("4", "Payment after 60 Days"),
    )
    customer_interest = models.ForeignKey(CustomerInterestModel, null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name="customer_interest_payment")
    bank_paid = models.CharField(max_length=254, choices=BANK_PAID, default="")
    amount_payable = models.DecimalField(decimal_places=4, max_digits=20, default=0.00)
    pay_reference = models.CharField(max_length=254, default="")
    payment_status = models.CharField(max_length=254, choices=PAYMENT_STATUS, default="")
    order_paid_by = models.CharField(max_length=254, default="")
    payment_terms = models.CharField(max_length=254, choices=PAYMENT_TERMS, default="")
    # date_overdue = models.DateField()
    farm = models.ForeignKey(FarmModel, null=True, blank=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="customer_payment_creator")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name="customer_payment_updater")

    def __str__(self):
        return self.pay_reference

    def get_absolute_url(self):
        return reverse("customer_payments:customer_payment_details", kwargs={"pk": self.id})




