from django.forms import ModelForm
from .models import FarmModel


class FarmCreateForm(ModelForm):

    class Meta:
        model = FarmModel
        fields = ['name', 'short_name', ]


class FarmUpdateForm(ModelForm):

    class Meta:
        model = FarmModel
        fields = ['name', 'short_name', ]
        # readonly = ()
