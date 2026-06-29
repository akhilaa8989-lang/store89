from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model=CustomerModel
        fields="__all__"

class productForm(forms.ModelForm):
    class Meta :
        model = productsModoel
        fields = "__all__"