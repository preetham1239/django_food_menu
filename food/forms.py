from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['item_desc'].widget.attrs.update({'class': 'form-control'})
        self.fields['item_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['item_image'].widget.attrs.update({'class': 'form-control'})
