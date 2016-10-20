from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Product
from .forms import ProductForm

'''
    PRODUCTS
'''
class ProductListView(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
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