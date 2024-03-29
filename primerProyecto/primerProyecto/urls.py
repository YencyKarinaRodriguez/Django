from django.contrib import admin
from django.urls import path
from miapp import views
import miapp.views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola_mundo/', views.hola_mundo, name="Hola Mundo"),
    path('saludo/', views.saludo, name="Saludo"),
    path('saludo/<int:redirigir>', views.saludo, name="Saludo"),
    path('presentacion/', views.presentacion, name="Presentacion"),
    path('', views.index, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('contacto/<str:nombre>', views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellido>', views.contacto, name="contacto"),
    path('quienesSomos/',views.quienesSomos, name="Quienes Somos"),
    path('productoServicios/',views.productoServicios, name="Productos y Servicios"),
    path('pagina/', miapp.views.pagina, name= "pagina"),
    path('crear_articulo/', miapp.views.crear_articulo, name = "crear_articulo"),
    path('crear_articulo/<str:title>/<str:content>/<str:public>', miapp.views.crear_articulo, name="crear_articulo"),
    path('articulo/', miapp.views.articulo, name = "Articulo"),
    path('editar_articulo/<int:id>', miapp.views.editar_articulo, name = "editar_articulo"),
    path('articulos/', miapp.views.articulos, name= "Listar"),
    path('borrarArticulo/<int:id>', miapp.views.borrarArticulo, name = "Borrar"),
    path('deleteArticulo/<int:id>', miapp.views.deleteArticulo, name = "eliminarSql"),
    path('updateArticulo/<str:title>/<int:id>', miapp.views.updateArticulo, name = "actualizarSql"),
    path('createArticulo/', miapp.views.createArticulo, name = "create"),
    path('saveArticulo/', miapp.views.saveArticulo, name= "save"),
    path('create-full-article/', miapp.views.create_full_articulo, name="create_full")
]
#configurar el titulo del panel
title="Master Blog de articulos"
admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title="Panel de Gestion"

#configuracion para cargar imagenes
if settings.DEBUG: #en el siguiente settings esta como true porque estamos local,
    #false cuando este en produccion
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#configurar el titulo del panel
admin.site.site_header="Master Blog de Articulos"
#configuracion para cargar imagenes
if settings.DEBUG:#en el settings esta como true porque estamos local,
    #false cuando este en produccion
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings)
