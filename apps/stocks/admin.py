from django.contrib import admin

from .models import StocksAdjustment, StocksAdjustmentItems
# Register your models here.

admin.site.register(StocksAdjustment)
admin.site.register(StocksAdjustmentItems)