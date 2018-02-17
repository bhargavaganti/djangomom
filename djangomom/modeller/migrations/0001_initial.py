# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-11-26 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelField',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.SlugField()),
                ('field_type', models.IntegerField(blank=True, choices=[(1, 'AutoField'), (2, 'IntegerField'), (3, 'FloatField'), (4, 'DateField'), (5, 'DateTimeField'), (6, 'EmailField'), (7, 'TimeField'), (8, 'DecimalField'), (9, 'CharField'), (10, 'SlugField'), (11, 'TextField'), (12, 'URLField'), (13, 'BigIntegerField'), (14, 'SmallIntegerField'), (15, 'PositiveSmallIntegerField'), (16, 'BooleanField'), (17, 'ForeignKey'), (18, 'ManyToManyField'), (19, 'OneToOneField'), (20, 'DurationField')])),
                ('max_length', models.IntegerField(blank=True, null=True)),
                ('default', models.CharField(blank=True, max_length=50, null=True)),
                ('blank', models.BooleanField(default=False)),
                ('null', models.BooleanField(default=True)),
                ('foreign_key', models.CharField(blank=True, max_length=100, null=True)),
                ('many_to_many_key', models.CharField(blank=True, max_length=50, null=True)),
                ('related_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelObject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.SlugField()),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.App')),
            ],
        ),
        migrations.CreateModel(
            name='QuerySet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('queryset_type', models.CharField(choices=[('LIST', 'List'), ('SINGLE', 'Single')], max_length=10)),
                ('reverse', models.BooleanField(default=False)),
                ('get_all', models.BooleanField(default=True)),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modeller.ModelObject')),
                ('order_paramater', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modeller.ModelField')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuerySetFilter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('filter_type', models.CharField(choices=[('exclude', 'Exclude'), ('filter', 'Include')], max_length=10)),
                ('operation', models.CharField(blank=True, choices=[('gte', 'Greater Than'), ('lte', 'Less Than'), ('contains', 'Contains'), ('exact', 'exact'), ('isnull', 'Is Null'), ('startswith', 'Starts With'), ('endswith', 'Ends With')], max_length=10, null=True)),
                ('filter_value', models.CharField(max_length=5000)),
                ('paramater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeller.ModelField')),
                ('queryset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeller.QuerySet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='modelfield',
            name='model_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modeller.ModelObject'),
        ),
        migrations.AlterUniqueTogether(
            name='modelobject',
            unique_together=set([('app', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='modelfield',
            unique_together=set([('model_obj', 'name')]),
        ),
    ]