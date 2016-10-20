from django.contrib import admin
from .models import Supplier, SupplierContact

class SupplierAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['supplier_name']}),
        ('Person', {'fields': ['supplier_contact_person'], 'classes': ['collapse']}),
        ('Other INFO', {
            'classes': ('collapse',),
            'fields': ('supplier_contact','email','created_date','updated_date','modified_by'),
        }),
    ]

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(SupplierContact)