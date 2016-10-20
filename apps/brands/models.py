from django.db import models
from django.utils import timezone

class Brand(models.Model):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    name = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
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
        return [(field.name, field.value_to_string(self)) for field in Brand._meta.fields]
