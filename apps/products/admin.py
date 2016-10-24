from django.contrib import admin
from .models import Product, ProductAttribute

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Created', {'fields': ['date_created'], 'classes': ['collapse']}),
        ('Publish Date', {'fields': ['date_publish'], 'classes': ['collapse']}),
        ('Other properties', {
            'classes': ('collapse',),
            'fields': ('barcode','brand','supplier','category','size_flag','price_cost','price_bought','price_wholesale','price_retail',
                       'free_shipping','order_min','order_max','desc_header','desc_body','image','remarks','tags','status','modified_by'),
        }),
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute)