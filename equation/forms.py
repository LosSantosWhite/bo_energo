from django.forms import ModelForm

from equation.models import Parameter


class ParameterForm(ModelForm):
    class Meta:
        model = Parameter
        fields = '__all__'
