from django.db import models

# Create your models here.


# tabla categoria del producto
class CategoriaProducto(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# tabla proveedor --> quien suministrea productos
class Proveedor(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Proveedores"


# tabla empleado --> quien hace  el movimiento del stock
class Empleado(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hiring_date = models.DateField()

    def __str__(self):
        return self.name


# tabla almacen
class Almacen(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Almacenes"


# tabla producto
class Producto(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_stock = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=50, default="unidad")
    category = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    supplier = models.ForeignKey(
        Proveedor, on_delete=models.SET_NULL, null=True, blank=True
    )
    store = models.ForeignKey(Almacen, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.current_stock} {self.unit})"


# tabla movimientoStock parecido a Factura
class MovimientoStock(models.Model):
    # para distinguir entre minus y mayus
    TIPO_CHOICES = [
        ("entrada", "Entrada"),
        ("salida", "Salida"),
    ]

    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    type_choice = models.CharField(max_length=10, choices=TIPO_CHOICES)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=100)  # Ej: Compra, Venta, Ajuste, Deterioro
    employee = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, null=True, blank=True
    )
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type_choice.capitalize()} de {self.amount} {self.product.name} - {self.date.strftime('%Y-%m-%d')}"

    def save(self, *args, **kwargs):
        # Si el movimiento ya existe (estamos editándolo)
        if self.pk is not None:
            # Obtenemos el estado anterior del movimiento desde la base de datos
            old = MovimientoStock.objects.get(pk=self.pk)

            # Revertimos su efecto en el stock del producto
            if old.type_choice == "entrada":
                self.product.current_stock -= old.amount
            elif old.type_choice == "salida":
                self.product.current_stock += old.amount

        # Aplicamos el nuevo movimiento
        if self.type_choice == "entrada":
            self.product.current_stock += self.amount
        elif self.type_choice == "salida":
            self.product.current_stock -= self.amount

        # Guardamos el nuevo stock del producto
        self.product.save()

        # Finalmente, guardamos el movimiento
        super().save(*args, **kwargs)
