# Generated by Django 5.0 on 2023-12-22 08:30

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_alter_invoicedetails_inv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='inv_id',
            field=models.BigIntegerField(default=builtins.id, unique=True),
        ),
    ]
