from django import forms

from orderapp.models import Order
from orderapp.services.validators import validate_city, validate_address, validate_postal_code


class OrderCreateForm(forms.ModelForm):
    city = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Введите город'}),
        validators=[validate_city]
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Введите адрес'}),
        validators=[validate_address]
    )
    postal_code = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Введите индекс'}),
        validators=[validate_postal_code]
    )
    class Meta:
        model = Order
        fields = 'city', 'address', 'postal_code'


    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-styling'
