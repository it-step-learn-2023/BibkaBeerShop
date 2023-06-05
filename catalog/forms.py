from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'about', 'category', 'producer', 'photo', 'quantitiy', 'displacement', 'price',)

class ProductForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'about', 'category', 'producer', 'quantitiy', 'displacement', 'price',)
