from django.db import models 

# Create your models here.

class Invoice(models.Model):
    inv_id = models.BigIntegerField(unique=True, null=False,default=3930)   
    date = models.DateTimeField(auto_now_add=True) 
    customer_name = models.CharField(max_length=255) 
    
    def save(self, *args, **kwargs):
        #self.inv_id = self.id 
        super().save(*args, **kwargs)     

class InvoiceDetails(models.Model):
    inv_id = models.ForeignKey(  
        Invoice, on_delete=models.CASCADE, to_field="inv_id", null=True  
    )       
    description = models.CharField(max_length=255,default='')
    quantity = models.IntegerField(null=True, default=0)
    unit_price = models.FloatField(null=True, default=0)
    price = models.FloatField(null=True, default=0)
    
    def save(self, *args, **kwargs):
        #self.id = int(self.inv_id.inv_id)  
        self.price = self.quantity * self.unit_price
        return super().save(*args, **kwargs)     


