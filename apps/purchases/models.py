from django.db import models
from django.utils import timezone
from products.models import Product
from suppliers.models import Supplier

class PurchaseOrder(models.Model):
    BOOL_CHOICES = ((True, 'Active'), (False, 'Inactive'))

    supplier = models.ForeignKey(Supplier, related_name='purchase_order_suppliers', on_delete=models.SET_NULL,null=True)
    total_cost = models.IntegerField(default=0, null=True)
    status = models.BooleanField(choices=BOOL_CHOICES, default=True)
    date_due = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    #created_by = models.ForeignKey('auth.User', null=True)
    modified_by = models.ForeignKey('auth.User', null=True)

    def __unicode__(self):
        return self.supplier

    def __str__(self):
        return self.supplier

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in PurchaseOrder._meta.fields]


class PurchaseOrderItems(models.Model):
    BOOL_CHOICES = ((True, 'Active'), (False, 'Inactive'))

    purchase_order = models.ForeignKey(PurchaseOrder, related_name='purchase_order_products', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name='purchase_products', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=False)
    cost = models.IntegerField(default=0, null=False)
    status = models.BooleanField(choices=BOOL_CHOICES, default=True)
    remarks = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.stock_adjustment

    def __str__(self):
        return self.stock_adjustment

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in PurchaseOrderItems._meta.fields]