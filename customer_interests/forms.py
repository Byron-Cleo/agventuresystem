from django.forms import ModelForm
from .models import CustomerInterestModel


class CustomerInterestCreateForm(ModelForm):

    class Meta:
        model = CustomerInterestModel
        fields = ['customer', 'crop_name', 'order_type', 'bag_type',
                  'ordered_quantity', 'cust_kg_price', 'farm_kg_price',
                  'total_bags', 'payment_terms', 'cust_dest']


class CustomerInterestUpdateForm(ModelForm):

    class Meta:
        model = CustomerInterestModel
        fields = ['customer', 'crop_name', 'order_type', 'bag_type',
                  'ordered_quantity', 'cust_kg_price', 'farm_kg_price',
                  'total_bags', 'farm_approval', 'payment_terms', 'cust_dest']
