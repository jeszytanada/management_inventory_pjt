from django import forms
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from .models import Supplier, SupplierContact

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        widgets = {
            'is_active': forms.RadioSelect
        }
        exclude = ('id',)
        fields = ['name','desc','tax_num','phone','fax','email','address','city','state','country','zipcode','image','url','tags','is_active']

    def clean(self):
        cleaned_data = super(SupplierForm, self).clean()
        return cleaned_data

class SupplierContactForm(forms.ModelForm):
    class Meta:
        model = SupplierContact
        exclude = ('id',)
        fields = ['first_name','last_name','supplier','email','phone','fax','mobile','dept','notes']

    def clean(self):
        cleaned_data = super(SupplierContactForm, self).clean()
        return cleaned_data