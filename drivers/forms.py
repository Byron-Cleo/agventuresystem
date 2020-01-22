from django.forms import ModelForm
from .models import DriverModel


class DriverCreateForm(ModelForm):

    class Meta:
        model = DriverModel
        fields = ['full_name', 'id_number', 'mobile_number', 'licence_number']


class DriverUpdateForm(ModelForm):

    class Meta:
        model = DriverModel
        fields = ['full_name', 'id_number', 'mobile_number', 'licence_number']
