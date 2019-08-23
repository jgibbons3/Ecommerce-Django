from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('viewClient/', views.ClientesList, name='viewClient'),
    path('viewProducts/', views.ProductosList, name='viewProducts'),
    path('viewInvoice/', views.InvoiceList, name='viewInvoice'),
    path('ProductDelete/<id>/', views.ProductDelete, name='delete'),
    path('ProductUpdate/<id>/', views.ProductUpdate, name='productUpdate'),
    path('ProductCreate/', views.ProductCreate, name='productCreate'),
    path('ProductInvoices/<id>/', views.ProductInvoices, name='ProductInvoices'),
    path('ClientInvoices/<id>/', views.ClientInvoices, name='ClientInvoices'),
    path('TopFiveClients', views.TopFiveClients, name='TopFiveClients'),
    path('TopFiveProducts', views.TopFiveProducts, name='TopFiveProducts'),
    path('', views.totalClientes, name='index'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)