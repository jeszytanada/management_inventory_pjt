from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import PurchaseOrder, PurchaseOrderItems

'''
    PURCHASES
'''
class PurchaseOrderView(ListView):
    template_name = 'purchases/purchase_order_list.html'
    context_object_name = 'purchase_order_list'

    def get_queryset(self):
        return PurchaseOrder.objects.all()

class PurchaseOrderDetailView(DetailView):
    model = PurchaseOrder
    template_name = 'purchases/purchase_order_detail.html'