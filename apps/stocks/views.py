from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import StocksAdjustment, StocksAdjustmentItems

'''
    STOCKS
'''
class StockAdjustmentView(ListView):
    template_name = 'stocks/stock_adjustment_list.html'
    context_object_name = 'stock_adjustment_list'

    def get_queryset(self):
        return StocksAdjustment.objects.all()

class StockAdjustmentDetailView(DetailView):
    model = StocksAdjustment
    template_name = 'stocks/stock_adjustment_detail.html'