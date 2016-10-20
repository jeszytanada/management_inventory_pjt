from django import forms
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from .models import Brand

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        widgets = {
            'is_active': forms.RadioSelect
        }
        exclude = ('id',)
        fields = ['name','desc','image','url','tags','is_active']

    def clean(self):
        cleaned_data = super(BrandForm, self).clean()
        return cleaned_data