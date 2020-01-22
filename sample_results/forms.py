from django.forms import ModelForm
from .models import (BarleySampleResultModel, WheatSampleResultModel,
                     PulsesSampleResultModel)


#########Barley Forms################
class BarleyCreateForm(ModelForm):

    class Meta:
        model = BarleySampleResultModel
        fields = ['moisture', 'nitrogen', 'rubbish', 'grain_size',
                  'extract', 'g_c', 'w_s', 'g_e', ]


class BarleyUpdateForm(ModelForm):

    class Meta:
        model = BarleySampleResultModel
        fields = ['moisture', 'nitrogen', 'rubbish', 'grain_size',
                  'extract', 'g_c', 'w_s', 'g_e', ]


#########Wheat Forms################
class WheatCreateForm(ModelForm):

    class Meta:
        model = WheatSampleResultModel
        fields = ['bushel', 'moisture', ]

class WheatCreateForm(ModelForm):

    class Meta:
        model = WheatSampleResultModel
        fields = ['bushel', 'moisture', ]


#########Pulses Forms################
class PulsesCreateForm(ModelForm):

    class Meta:
        model = PulsesSampleResultModel
        fields = ['color', ]

class PulsesCreateForm(ModelForm):

    class Meta:
        model = PulsesSampleResultModel
        fields = ['color', ]
