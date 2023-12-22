# Generated by Django 5.0 on 2023-12-22 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_id', models.IntegerField(default=10303, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('unit_price', models.FloatField(default=0, null=True)),
                ('price', models.FloatField(default=0, null=True)),
                ('inv', models.ForeignKey(default=10303, on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice', to_field='inv_id')),
            ],
        ),
    ]
