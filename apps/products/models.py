from django.db import models
from django.utils import timezone
from category.models import Category
from brands.models import Brand
from suppliers.models import Supplier

class Product(models.Model):
    BOOL_CHOICES = ((True, 'active'), (False, 'inactive'))
    REGULAR = 'Regular'
    SAMPLE = 'Sample'
    TESTER = 'Tester'
    OTHERS = 'Others'

    SIZE_FLAG_CHOICES = (
        (REGULAR, 'Regular'),
        (SAMPLE, 'Sample'),
        (TESTER, 'Tester'),
        (OTHERS, 'Others'),
    )

    ALWAYS = 'Always'
    NORMAL = 'Normal'
    SPECIAL = 'Special'
    FREE_SHIPPING_CHOICES = (
        (ALWAYS, 'Always'),
        (NORMAL, 'Normal'),
        (SPECIAL, 'Special')
    )
    barcode = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, related_name='brands', on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, related_name='suppliers', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.SET_NULL, null=True)
    size_flag = models.CharField(max_length=7, choices=SIZE_FLAG_CHOICES, default=REGULAR)
    price_cost = models.FloatField(default=0)
    price_bought = models.FloatField(default=0)
    price_wholesale = models.FloatField(default=0)
    price_retail = models.FloatField(default=0)
    free_shipping = models.CharField(max_length=7, choices=FREE_SHIPPING_CHOICES, null=True)
    order_min = models.IntegerField(default=1)
    order_max = models.IntegerField(default=1)
    desc_header = models.CharField(max_length=100, blank=True)
    desc_body = models.TextField(blank=True)
    status = models.BooleanField(choices=BOOL_CHOICES, default=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    date_publish = models.DateTimeField(blank=True, null=True)
    modified_by = models.ForeignKey('auth.User', null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Product._meta.fields]

class ProductAttribute(models.Model):
    COLOR = 'Color'
    SIZE = 'Size'
    WEIGHT = 'Weight'
    TYPE_CHOICES = (
        (COLOR, 'Color'),
        (SIZE, 'Size'),
        (WEIGHT, 'Weight')
    )
    product = models.ForeignKey(Product, related_name='product_attr', on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default=COLOR)
    value = models.CharField(max_length=80)

    def __str__(self):
        return self.product_attr.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ProductAttribute._meta.fields]


class ProductStock(models.Model):
    product = models.ForeignKey(Product, related_name='product_stock', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_stock.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ProductStock._meta.fields]


class ProductStockHistory(models.Model):
    product = models.ForeignKey(Product, related_name='product_stock_history', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    reference_type = models.IntegerField(default=0)
    reference_id = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_stock.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ProductStockHistory._meta.fields]