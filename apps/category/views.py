from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from products.models import Product
from .models import Category
from .forms import CategoryForm

'''
    CATEGORY
'''

class CategoryListView(ListView):
    template_name = 'category/category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        #return Category.objects.filter(is_child=False).exclude(id=11)
        # Get all Category with None[11] as parent_id and exclude None from list
        return Category.objects.filter(parent_id=1).exclude(id=1)


class CategorySubListView(ListView):
    template_name = 'category/category_sub_list.html'
    context_object_name = 'category_sub_list'

    def get_queryset(self):
        return Category.objects.filter(parent_id=self.kwargs.get('pk'))

    def get_context_data(self, *args, **kwargs):
        context = super(CategorySubListView, self).get_context_data(*args, **kwargs)
        context['category_products'] = Product.objects.filter(category=self.kwargs.get('pk'))
        return context


class CategoryProductListView(ListView):
    template_name = 'category/category_product.html'
    context_object_name = 'category_products'

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs.get('pk'))

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryProductListView, self).get_context_data(*args, **kwargs)
        context['category_sub_list'] = Category.objects.filter(parent_id=self.kwargs.get('pk'))
        return context


class CategoryCreate(CreateView):
    model = Category
    template_name = 'category/category_add.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:category_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(CategoryCreate, self).form_valid(form)
        else:
            form = CategoryForm()
            return render(self, 'category/category_add.html', {'form': form})


class CategoryEdit(UpdateView):
    model = Category
    template_name = 'category/category_edit.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:category_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(CategoryEdit, self).form_valid(form)
        else:
            form = CategoryForm()
            return render(self, 'category/category_edit.html', {'form': form})
