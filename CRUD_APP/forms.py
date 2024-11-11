from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'eid':'E ID',
            'ename':'E NAME',
            'emobile':'E MOBILE',
            'email':'E MAIL',
            'eaddress':'E ADDRESS',
            'edate':'E DATE'
        }
        widgets = {
            'edate': forms.DateInput(attrs={'type':'date'}),
            'eaddress': forms.Textarea()
        }