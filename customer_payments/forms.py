from django.forms import ModelForm
from .models import CustomerPaymentModel


class CustomerPaymentCreateForm(ModelForm):

    class Meta:
        model = CustomerPaymentModel
        fields = ['bank_paid', 'amount_payable', 'pay_reference',
                  'payment_status', 'order_paid_by', 'payment_terms']
        exclude =['payment_overdue']


class CustomerPaymentUpdateForm(ModelForm):

    class Meta:
        model = CustomerPaymentModel
        fields = ['bank_paid', 'amount_payable', 'pay_reference',
                  'payment_status', 'order_paid_by', 'payment_terms']