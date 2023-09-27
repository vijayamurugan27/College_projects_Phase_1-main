from django import forms
from .models import PhotoGraphy



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
