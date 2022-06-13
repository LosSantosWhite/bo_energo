from django.forms import ModelForm
from assignment.models import Item, Color


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["number"]
