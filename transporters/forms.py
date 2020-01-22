from django.forms import ModelForm
from .models import TransportModel


class TransporterCreateForm(ModelForm):

    class Meta:
        model = TransportModel
        fields = ['name', 'contract_status'] #address


class TransporterUpdateForm(ModelForm):

    class Meta:
        model = TransportModel
        fields = ['name', 'contract_status'] #address
