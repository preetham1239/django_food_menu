from django import forms
from .models import FoodItem

class FoodItemForm(forms.ModelForm):
    """
    This class is used to create a form for the FoodItem model. The fields are the attributes of the FoodItem model.
    """
    class Meta:
        """
        This class is used to define the model and the fields of the model that will be used in the form.
        Django will automatically create the form fields for the model fields.
        """
        model = FoodItem
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']

    def __init__(self, *args, **kwargs):
        """
        This method is used to add attributes to the form fields. In this case, the class attribute is added to the form fields.
        They are added to the form fields so that the Bootstrap classes can be used to style the form fields.
        """
        super().__init__(*args, **kwargs)
        self.fields['item_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['item_desc'].widget.attrs.update({'class': 'form-control'})
        self.fields['item_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['item_image'].widget.attrs.update({'class': 'form-control'})
