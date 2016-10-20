# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-20 06:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20161020_1049'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StocksAdjustment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.IntegerField(default=0, null=True)),
                ('reference_type', models.CharField(max_length=100)),
                ('reason', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(default=0, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StocksAdjustmentItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_products', to='products.Product')),
                ('stock_adjustment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_adjustments', to='stocks.StocksAdjustment')),
            ],
        ),
    ]
