from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Product
from .forms import ProductForm, SearchForm
import operator

'''
    PRODUCTS
'''
class ProductListView(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'
    form_class = SearchForm

    def get_queryset(self):
        return Product.objects.all()

    # Manual Search Filter
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        context['product_search_list'] = {
            'form': SearchForm()
        }
        return context

class ProductSearchListView(ListView):
    template_name = 'products/product_search_list.html'
    form_class = SearchForm
    context_object_name = 'product_search_list'

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['name']:
                return Product.objects.filter(name__icontains=form.cleaned_data['name'])
            if form.cleaned_data['barcode']:
                return Product.objects.filter(barcode__icontains=form.cleaned_data['barcode'])
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/product_add.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(ProductCreate, self).form_valid(form)
        else:
            form = ProductForm()
            return render(self, 'products/product_add.html', {'form': form})


class ProductEdit(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_edit.html'
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form_class):
        if form_class.is_valid():
            form_class.save()
            instance = form_class.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(ProductEdit, self).form_valid(form_class)
        else:
            form = ProductForm()
            return render(self, 'products/product_edit.html', {'form': form})


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('products:index')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)