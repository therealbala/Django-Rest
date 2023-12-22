from django.contrib import admin
from django.urls import path,include 
from . import views  


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('invoices/', include('invoice.urls')),   
    path('invoices', include('invoice.urls')),  
    path('',views.home) 
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'Myinv.views.custom_404'  