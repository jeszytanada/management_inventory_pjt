from django.db import models
from django.utils import timezone

class CategoryDescription(models.Model):
    categories_name = models.CharField(max_length=100)
    categories_description = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('auth.User', null=True)

    def __str__(self):
        return self.categories_name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in CategoryDescription._meta.fields]

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    is_child = models.BooleanField(default=False)
    parent = models.ForeignKey("self", default=11)
    #parent = models.ForeignKey(CategoryDescription, related_name='prime_category', default=0)
    image = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('auth.User', null=True)


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Category._meta.fields]
