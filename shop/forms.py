from django import forms

from shop.models import Products, Customer


class ShopProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

class ShopOrderForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['order_status', 'items']

