from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework.response import Response 
from .models import Invoice,InvoiceDetails  
from .serializer import InvoiceSerializer
# Create your views here.
 
from django.views.decorators.csrf import csrf_exempt   
from rest_framework.decorators import api_view 
from django.db.models import Avg, Max, Min, Sum 
#from .serializer import InvoiceSerializer 

# Create your views here.
#@csrf_exempt    
@api_view(['POST','GET'])    
def home_inv(request): 
    if request.method == "GET": 
        mydata = Invoice.objects.all().values()  
        return render(request, "invoice.html", {'mydata':mydata})  
    elif request.method == "POST": 
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
           jsonf = request.data  
           try: 
                cus_name = str(jsonf['name'])  
                description = str(jsonf['description']) 
                quantity = int(jsonf['quantity'])
                price = float(jsonf['price'])
                unit_price = float(jsonf['unit_price'])

                ##max_rated_entry = Invoice.objects.last().inv_id+1   
                try: 
                   max_rated_entry = Invoice.objects.order_by('-inv_id').first().inv_id+1    
                except:
                   max_rated_entry = 1043 
                Invv = Invoice.objects.create(customer_name=cus_name,inv_id=max_rated_entry,)
                Invv.save() 
                Invv = InvoiceDetails.objects.create(description=description,inv_id=Invoice.objects.get(inv_id=max_rated_entry),
                                                    quantity=quantity,unit_price=unit_price,
                                                    price=price)
                Invv.save()  
                return  Response(f'Record successfully added')    
           except: 
                return Response('Error')

@api_view(['POST','GET'])              
def inv(request,pk):   
    if request.method == "GET":  
        mydata = Invoice.objects.filter(inv_id=pk).values()
        if len(mydata)!=0:
            mydata = mydata[0] 
        else: 
            return HttpResponse(" No Invoice Found ")
        my_inv =  mydata['inv_id'] 
        try:
           mydata2 = InvoiceDetails.objects.filter(inv_id=my_inv).values()[0]  
        except: 
           idx = InvoiceDetails(
                inv_id=Invoice.objects.get(inv_id = my_inv) ,description='')     
           idx.save() 

           mydata2 = InvoiceDetails.objects.filter(inv_id=my_inv).values()[0]  
        mydata = dict(mydata.items() | mydata2.items())
        return render(request, "inv.html", {'mydata':mydata})  
    else: 
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
           jsonf = request.data  
           try:  
                description = str(jsonf['description']) 
                quantity = int(jsonf['quantity'])
                price = float(jsonf['price'])
                unit_price = float(jsonf['unit_price']) 
      
                ##Invv = InvoiceDetails.objects.create(description=description,inv_id=Invoice.objects.get(inv_id=max_rated_entry),
                #                                    quantity=quantity,unit_price=unit_price,
                #                                    price=price)   
                mydata = Invoice.objects.filter(inv_id=pk).values()
                if len(mydata)!=0:
                    mydata = mydata[0] 
                else: 
                    return Response(" No Invoice Found ")
                my_inv =  mydata['inv_id'] 
        
                obj = Invoice.objects.get(inv_id=my_inv)
                obj.description = description 
                onj.quantity = quantity 
                obj.price = price 
                obj.unit_price = unit_price 
                obj.save()   
                return  Response(f'Record Updated added')    
           except: 
                return Response(str(my_inv))
 
        

