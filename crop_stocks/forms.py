from django.forms import ModelForm
from .models import CropStockModel


class CropStockCreateForm(ModelForm):

    class Meta:
        model = CropStockModel
        fields = ['name', 'variety', 'grade', ]


class CropStockUpdateForm(ModelForm):

    class Meta:
        model = CropStockModel
        fields = ['name', 'variety', 'grade', ]
