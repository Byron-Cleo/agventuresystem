from django.forms import ModelForm
from .models import TruckModel


class TruckCreateForm(ModelForm):

    class Meta:
        model = TruckModel
        fields = fields = ['transporter', 'max_weight', 'truck_type', 'reg_number', 'chassis_number', 'color'] #address


class TruckUpdateForm(ModelForm):

    class Meta:
        model = TruckModel
        fields = ['transporter', 'max_weight', 'truck_type', 'reg_number', 'chassis_number', 'color'] #address
