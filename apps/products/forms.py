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

# class FileUploadForm(forms.Form):
#
#     file = forms.FileField()
#
#     def clean_file(self):
#         data = self.cleaned_data["file"]
#         # read and parse the file, create a Python dictionary `data_dict` from it
#         form = ProductForm(data_dict)
#         if form.is_valid():
#             # we don't want to put the object to the database on this step
#             self.instance = form.save(commit=False)
#         else:
#             # You can use more specific error message here
#             raise forms.ValidationError(u"The file contains invalid data.")
#         return data
#
#     def save(self):
#         # We are not overriding the `save` method here because `form.Form` does not have it.
#         # We just add it for convenience.
#         instance = getattr(self, "instance", None)
#         if instance:
#             instance.save()
#         return instance

class SearchForm(ModelForm):

    def __init__(self, *args, **kwargs):
        # call parent's constructor
        super(SearchForm, self).__init__(*args, **kwargs)
        # fields property
        self.fields['name'].required = False
        self.fields['barcode'].required = False

    class Meta:
        model = Product
        fields =('name','barcode',)

    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        return cleaned_data