from django.db import models
from django.utils import timezone

class Supplier(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
    tax_num = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=False, default='000-0000')
    fax = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(choices=BOOL_CHOICES, default=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Supplier._meta.fields]


class SupplierContact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, related_name='supplier_contacts', on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    notes = models.TextField(null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.first_name