from django.contrib import admin
from django.urls import path
from General.views import home
#from django.views.generic import TemplateView
from General.views import *
#  ProductosListado, ProductosDetalle, ProductosCrear, ProductosActualizar, ProductosEliminar, views
#from . import views
 

 
from django.conf import settings
from django.conf.urls.static import static 
 
urlpatterns = [
    #path('', home.as_view(template_name='General/index.html'), name = 'home'),
    # path('general/leer', ProductosListado.as_view(), name='leer'),
    # path('general/detalle/<int:pk>', ProductosDetalle.as_view(template_name = "general/detalles.html"), name='detalles'), 
    # path('general/crear', ProductosCrear.as_view(template_name = "general/crear.html"), name='crear'),
    # path('general/editar/<int:pk>', ProductosActualizar.as_view(template_name = "general/editar.html"), name='editar'),    
    # path('general/eliminar/<int:pk>', ProductosEliminar.as_view(), name='eliminar'),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
