from django.forms import ModelForm
from .models import TrailerModel


class TrailerCreateForm(ModelForm):

    class Meta:
        model = TrailerModel
        fields = ['transporter', 'reg_number', 'chassis_number', 'color'] #logbook_scan_image trailer_image


class TrailerUpdateForm(ModelForm):

    class Meta:
        model = TrailerModel
        fields = ['transporter', 'reg_number', 'chassis_number', 'color'] #logbook_scan_image trailer_image
