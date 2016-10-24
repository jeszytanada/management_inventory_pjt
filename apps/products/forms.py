from django.utils import timezone
from datetime import date
from django import forms
from django.forms import ModelForm
from .models import Product
from django.contrib.admin import widgets
from .models import Product


class ProductForm(ModelForm):

    class Meta:
        model = Product
        widgets = {
            'date_publish': forms.DateInput(attrs={'class': 'datepicker'}),
        }
        exclude = ('id',)
        fields = ['barcode', 'name', 'brand', 'supplier', 'category', 'size_flag', 'price_cost', 'price_bought',
                  'price_wholesale', 'price_retail','free_shipping', 'order_min', 'order_max', 'desc_header',
                  'desc_body', 'image', 'remarks', 'tags','status', 'date_publish']

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        return cleaned_data

class SearchForm(ModelForm):

    class Meta:
        model = Product
        fields =['name','barcode',]

    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        return cleaned_data