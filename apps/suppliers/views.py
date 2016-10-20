from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Supplier, SupplierContact
from .forms import SupplierForm, SupplierContactForm

'''
    SUPPLIERS
'''
class SupplierListView(ListView):
    template_name = 'suppliers/supplier_list.html'
    context_object_name = 'supplier_list'

    def get_queryset(self):
        return Supplier.objects.all()


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'suppliers/supplier_detail.html'


class SupplierEdit(UpdateView):
    model = Supplier
    template_name = 'suppliers/supplier_edit.html'
    form_class = SupplierForm
    success_url = reverse_lazy('suppliers:supplier_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(SupplierEdit, self).form_valid(form)
        else:
            form = SupplierForm()
            return render(self, 'suppliers/supplier_edit.html', {'form': form})


class SupplierDelete(DeleteView):
    model = Supplier
    template_name = 'suppliers/supplier_delete.html'
    success_url = reverse_lazy('suppliers:supplier_list')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)


class SupplierCreate(CreateView):
    model = Supplier
    template_name = 'suppliers/supplier_add.html'
    form_class = SupplierForm
    success_url = reverse_lazy('suppliers:supplier_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(SupplierCreate, self).form_valid(form)
        else:
            form = SupplierForm()
            return render(self, 'suppliers/supplier_add.html', {'form': form})


'''
    SUPPLIER CONTACTS
'''
class SupplierContactListView(ListView):
    template_name = 'suppliers/supplier_contact_list.html'
    context_object_name = 'supplier_contact_list'

    def get_queryset(self):
        supplier = Supplier.objects.get(pk=self.kwargs.get('pk'))
        return supplier.supplier_contacts.all()


class SupplierContactCreate(CreateView):
    model = SupplierContact
    template_name = 'suppliers/supplier_contact_add.html'
    form_class = SupplierContactForm
    success_url = reverse_lazy('suppliers:supplier_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(SupplierContactCreate, self).form_valid(form)
        else:
            form = SupplierContactForm()
            return render(self, 'suppliers/supplier_contact_add.html', {'form': form})


class SupplierContactEdit(UpdateView):
    model = SupplierContact
    template_name = 'suppliers/supplier_contact_edit.html'
    form_class = SupplierContactForm
    success_url = reverse_lazy('suppliers:supplier_list')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            instance = form.instance
            instance.modified_by = self.request.user
            instance.save()
            return super(SupplierContactEdit, self).form_valid(form)
        else:
            form = SupplierContactForm()
            return render(self, 'suppliers/supplier_contact_edit.html', {'form': form})