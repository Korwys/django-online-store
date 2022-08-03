from django import forms

from orderapp.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'city', 'adress', 'postal_code'

    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-styling'
