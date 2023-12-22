from rest_framework import serializers
from .models import Invoice,InvoiceDetails 

class InvoiceSerializer(serializers.ModelSerializer):
  class Meta:
    model=Invoice
    fields=('inv_id','date','customer_name')