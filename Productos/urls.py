from django.contrib import admin
from django.urls import path

#from django.views.generic import TemplateView
from Productos.views import *
#  ProductosListado, ProductosDetalle, ProductosCrear, ProductosActualizar, ProductosEliminar, views
#from . import views
 

 
from django.conf import settings
from django.conf.urls.static import static 
 
urlpatterns = [
    # path('', home.as_view(template_name='General/index.html'), name = 'home'),
    path('Productos/leer', ProductosListado.as_view(template_name ="Productos/productos.html"), name='leer'),
    path('Productos/detalle/<int:pk>', ProductosDetalle.as_view(template_name = "Productos/detalles.html"), name='detalles'), 
    path('Productos/crear', ProductosCrear.as_view(template_name = "Productos/crear.html"), name='crear'),
    path('Productos/editar/<int:pk>', ProductosActualizar.as_view(template_name = "Productos/editar.html"), name='editar'),    
    path('Productos/eliminar/<int:pk>', ProductosEliminar.as_view(), name='eliminar'),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
