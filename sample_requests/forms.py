from django.forms import ModelForm
from .models import SampleRequestModel


class SampleRequestModelCreateForm(ModelForm):

    class Meta:
        model = SampleRequestModel
        fields = ['crop_requested', 'sample_quantity',
                  'delivery_destination', 'request_status', ]


class SampleRequestUpdateForm(ModelForm):

    class Meta:
        model = SampleRequestModel
        fields = ['crop_requested', 'sample_quantity',
                  'delivery_destination', 'request_status', ]
