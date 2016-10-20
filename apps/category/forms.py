from django import forms
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('id',)
        #fields = ['categories_name','categories_description','tags','date_created','date_updated','modified_by']
        fields = ['name', 'description', 'is_child', 'parent', 'image', 'tags']

    def clean(self):
        cleaned_data = super(CategoryForm, self).clean()
        return cleaned_data