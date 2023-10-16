
from django.contrib import admin
from django.urls import path
from gestionproductos import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_productos, name='lista_productos'),
    path('<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
