from django.db import models

class Producto(models.Model):
    sku = models.CharField(primary_key=True, max_length=20, unique=True)
    nombre = models.CharField(max_length=60)
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sku} {self.nombre} {self.precio} {self.cantidad}"

class Cliente(models.Model):
    nombre_usuario = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100)
    rut = models.CharField(max_length=10, primary_key=True, unique=True)
    numero_documento = models.CharField(max_length=9)
    contraseña = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.nombre_usuario} {self.correo} {self.rut} {self.numero_documento}"

class Movimiento(models.Model):
    TIPO_CHOICES = [('S', 'Salida'), ('E', 'Entrada')]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_movimiento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} {self.cantidad} {self.fecha_movimiento} {self.producto}"

class Boleta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    detalle = models.JSONField()
    total = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} {self.total}"