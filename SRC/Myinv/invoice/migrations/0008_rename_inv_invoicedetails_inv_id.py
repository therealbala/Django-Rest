# Generated by Django 5.0 on 2023-12-22 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_rename_inv_id_invoicedetails_inv'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoicedetails',
            old_name='inv',
            new_name='inv_id',
        ),
    ]
