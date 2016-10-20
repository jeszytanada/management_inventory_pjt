from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Brand
from .forms import BrandForm

# class IndexView(TemplateView):
#     template_name = "brands/index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         context['latest_product'] = Brand.objects.all()[:1]
#         return context
'''
    BRANDS
'''
class BrandListView(ListView):
    template_name = 'brands/brand_list.html'
    context_object_name = 'brand_list'

    def get_queryset(self):
        return Brand.objects.all()


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand_detail.html'


class BrandCreate(CreateView):
    model = Brand
    template_name = 'brand_add.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(BrandCreate, self).form_valid(form)
        else:
            form = BrandForm()
            return render(self, 'brand_add.html', {'form': form})


class BrandEdit(UpdateView):
    model = Brand
    template_name = 'brand_edit.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(BrandEdit, self).form_valid(form)
        else:
            form = BrandForm()
            return render(self, 'brand_edit.html', {'form': form})


class BrandDelete(DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)
