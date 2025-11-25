from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    color = models.CharField(max_length=20)
    tipo_combustible = models.CharField(max_length=50)
    kilometraje = models.IntegerField()
    precio_venta = models.DecimalField(max_digits=15, decimal_places=2)
    estado_auto = models.CharField(max_length=50)
    num_vin = models.CharField(max_length=50)
    fecha_ingreso_concesionaria = models.DateField()
    tipo_transmision = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"


class ClienteConcesionaria(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    dni = models.CharField(max_length=20)
    fecha_registro = models.DateField()
    presupuesto_maximo = models.DecimalField(max_digits=15, decimal_places=2)
    preferencias_auto = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_contratacion = models.DateField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    comision_porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    dni = models.CharField(max_length=20)
    num_ventas_mes = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class TallerAsociado(models.Model):
    nombre_taller = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    persona_contacto = models.CharField(max_length=100)
    especialidades = models.TextField()
    horario_atencion = models.TextField()

    def __str__(self):
        return self.nombre_taller


class ServicioPostventa(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo_estandar = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_horas = models.IntegerField()
    requiere_cita = models.BooleanField()
    tipo_mantenimiento = models.CharField(max_length=100)
    taller_asociado = models.ForeignKey(TallerAsociado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_servicio


class VentaAuto(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(ClienteConcesionaria, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField()
    precio_final_venta = models.DecimalField(max_digits=15, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    tiene_financiamiento = models.BooleanField()
    fecha_entrega_auto = models.DateField()
    garantia_meses = models.IntegerField()

    def __str__(self):
        return f"Venta #{self.id}"


class CitaServicio(models.Model):
    cliente = models.ForeignKey(ClienteConcesionaria, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    servicio = models.ForeignKey(ServicioPostventa, on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    estado_cita = models.CharField(max_length=50)
    comentarios_cliente = models.TextField()
    fecha_finalizacion_servicio = models.DateTimeField()

    def __str__(self):
        return f"Cita #{self.id}"
