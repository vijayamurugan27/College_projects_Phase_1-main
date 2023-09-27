from .models import Foods
from django import forms  


class ProductForm(forms.ModelForm):
    class Meta:
        model = Foods
        fields = "__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model = Foods
        fields = ['order_status', 'items']
