# Generated by Django 5.0.4 on 2024-05-04 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'SalesTypes',
            },
        ),
        migrations.CreateModel(
            name='ForSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_type', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('comments', models.TextField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.salestypes')),
            ],
            options={
                'db_table': 'ForSale',
            },
        ),
        migrations.CreateModel(
            name='ForRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_type', models.CharField(max_length=300)),
                ('rent_per_month', models.FloatField()),
                ('comments', models.TextField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.salestypes')),
            ],
            options={
                'db_table': 'ForRent',
            },
        ),
    ]