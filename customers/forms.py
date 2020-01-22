from django.forms import ModelForm
from .models import CustomerModel


class CustomerCreateForm(ModelForm):

    class Meta:
        model = CustomerModel
        fields = ['name', 'type', 'category', 'department',
                  'payment_terms', 'currency', 'reg_no', 'vat_reg', ]


class CustomerUpdateForm(ModelForm):

    class Meta:
        model = CustomerModel
        fields = ['name', 'type', 'category', 'department',
                  'payment_terms', 'currency', 'reg_no', 'vat_reg', ]
