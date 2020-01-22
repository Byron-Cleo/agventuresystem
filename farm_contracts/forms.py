from django.forms import ModelForm
from .models import FarmContractModel


class FarmContractCreateForm(ModelForm):

    class Meta:
        model = FarmContractModel
        fields = ['buyer', 'customer_contract', 'farm_tolerance', 'delivery_weigh_bridge',
                  'delivery_period', 'quality_specs', 'rejection_procedure', 'weighing_conditions',
                  'offloading_fees', 'governing_terms', 'whole_agreement']


class FarmContractUpdateForm(ModelForm):

    class Meta:
        model = FarmContractModel
        fields = ['buyer', 'customer_contract', 'farm_tolerance', 'delivery_weigh_bridge',
                  'delivery_period', 'quality_specs', 'rejection_procedure', 'weighing_conditions',
                  'offloading_fees', 'governing_terms', 'whole_agreement']
