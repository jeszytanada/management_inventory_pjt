from django.contrib import admin

from .models import PurchaseOrder, PurchaseOrderItems
# Register your models here.

admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItems)
