from django.db import models
from django.contrib.auth.models import User  # Importa el modelo User de Django

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    # Agrega otros campos relacionados con el proveedor si es necesario

class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    calidad = models.CharField(max_length=100)
    datos_fisicoquimicos = models.TextField()

    # Agrega campos para el análisis físicoquímico y el usuario que realizó la acción
    analisis_imagen = models.ImageField(upload_to='analisis_leche/', null=True, blank=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def guardar(self, *args, **kwargs):
        # Sobreescribe el método save para rastrear al usuario que realiza la acción
        if self.pk:
            # El objeto ya existe, lo que indica una actualización
            self.usuario_modificacion = User.objects.get(username='nombre_de_usuario_logueado')
        else:
            # El objeto se está creando por primera vez
            self.usuario_modificacion = User.objects.get(username='nombre_de_usuario_logueado')

        super(Producto, self).save(*args, **kwargs)
