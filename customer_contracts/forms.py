from django.forms import ModelForm
from .models import CustomerContractModel


class CustomerContractCreateForm(ModelForm):

    class Meta:
        model = CustomerContractModel
        fields = ['customer', 'seller', 'cust_tolerance', 'quality_specs',
                  'delivery_period', 'rejection_procedure', 'delivery_terms', 'offloading_fees',
                  'governing_terms', 'whole_agreement']


class CustomerContractUpdateForm(ModelForm):

    class Meta:
        model = CustomerContractModel
        fields = ['customer', 'seller', 'cust_tolerance', 'quality_specs',
                  'delivery_period', 'rejection_procedure', 'delivery_terms', 'offloading_fees',
                  'governing_terms', 'whole_agreement']
