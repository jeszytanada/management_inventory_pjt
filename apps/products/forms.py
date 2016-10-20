from django import forms
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('id',)
        fields = ['barcode','name','brand','supplier','category','size_flag','price_cost','price_bought','price_wholesale','price_retail',
                  'free_shipping','order_min','order_max','desc_header','desc_body','image','remarks','tags','status','date_publish']

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        return cleaned_data