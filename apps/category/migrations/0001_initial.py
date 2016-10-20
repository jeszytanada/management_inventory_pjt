# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-18 08:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_child', models.BooleanField(default=False)),
                ('image', models.TextField(blank=True, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories_name', models.CharField(max_length=100)),
                ('categories_description', models.TextField(blank=True, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
