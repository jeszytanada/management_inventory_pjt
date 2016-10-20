from django.db import models
from django.utils import timezone
from products.models import Product

class StocksAdjustment(models.Model):

    reference = models.IntegerField(default=0, null=True)
    reference_type = models.CharField(max_length=100)
    reason = models.TextField(blank=True, null=True)
    type = models.IntegerField(default=0, null=True)
    remarks = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('auth.User', null=True)

    def __unicode__(self):
        return self.reference

    def __str__(self):
        return self.reference

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in StocksAdjustment._meta.fields]


class StocksAdjustmentItems(models.Model):

    stock_adjustment = models.ForeignKey(StocksAdjustment, related_name='stock_adjustments', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name='stock_products', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=False)
    remarks = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.stock_adjustment

    def __str__(self):
        return self.stock_adjustment

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in StocksAdjustmentItems._meta.fields]