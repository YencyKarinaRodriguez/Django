from django.contrib import admin
from django.urls import path
from miapp import views
import miapp.views

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
    path('pagina/', miapp.views.pagina, name= "pagina") 
]
