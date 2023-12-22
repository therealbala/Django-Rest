from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)  
    #return HttpResponse("hi")    

def home(request):
    return render(request, '404.html', status=404)    
    

