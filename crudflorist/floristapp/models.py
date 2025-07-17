from django.db import models
from django.core.exceptions import ValidationError


# =========================
# Modelo: Categoría Producto
# =========================
class CategoriaProducto(models.Model):
    name = models.CharField("Nombre", max_length=100)

    class Meta:
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"
        ordering = ["name"]

    def __str__(self):
        return self.name


# =========================
# Modelo: Proveedor
# =========================
class Proveedor(models.Model):
    name = models.CharField("Nombre", max_length=150)
    phone = models.CharField("Teléfono", max_length=20)
    email = models.EmailField("Correo electrónico")
    address = models.TextField("Dirección")

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ["name"]

    def __str__(self):
        return self.name


# =========================
# Modelo: Empleado
# =========================
class Empleado(models.Model):
    name = models.CharField("Nombre", max_length=100)
    position = models.CharField("Cargo", max_length=100)
    hiring_date = models.DateField("Fecha de contratación")

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["name"]

    def __str__(self):
        return self.name


# =========================
# Modelo: Almacén
# =========================
class Almacen(models.Model):
    name = models.CharField("Nombre", max_length=100)
    location = models.CharField("Ubicación", max_length=200)

    class Meta:
        verbose_name = "Almacén"
        verbose_name_plural = "Almacenes"
        ordering = ["name"]

    def __str__(self):
        return self.name


# =========================
# Modelo: Producto
# =========================
class Producto(models.Model):
    name = models.CharField("Nombre", max_length=150)
    description = models.TextField("Descripción", blank=True)
    purchase_price = models.DecimalField(
        "Precio de compra", max_digits=10, decimal_places=2
    )
    sales_price = models.DecimalField(
        "Precio de venta", max_digits=10, decimal_places=2
    )
    current_stock = models.PositiveIntegerField("Stock actual", default=0)
    unit = models.CharField("Unidad", max_length=50, default="unidad")
    category = models.ForeignKey(
        CategoriaProducto, on_delete=models.CASCADE, verbose_name="Categoría"
    )
    supplier = models.ForeignKey(
        Proveedor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Proveedor",
    )
    store = models.ForeignKey(
        Almacen,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Almacén",
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.current_stock} {self.unit})"


# =========================
# Modelo: Movimiento de Stock
# =========================
class MovimientoStock(models.Model):
    TIPO_CHOICES = [
        ("entrada", "Entrada"),
        ("salida", "Salida"),
    ]

    product = models.ForeignKey(
        Producto, on_delete=models.CASCADE, verbose_name="Producto"
    )
    type_choice = models.CharField(
        "Tipo de movimiento", max_length=10, choices=TIPO_CHOICES
    )
    amount = models.PositiveIntegerField("Cantidad")
    date = models.DateTimeField("Fecha", auto_now_add=True)
    reason = models.CharField("Motivo", max_length=100)
    employee = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Empleado",
    )
    observaciones = models.TextField("Observaciones", blank=True, null=True)

    class Meta:
        verbose_name = "Movimiento de Stock"
        verbose_name_plural = "Movimientos de Stock"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.type_choice.capitalize()} de {self.amount} {self.product.name} - {self.date.strftime('%Y-%m-%d')}"

    def save(self, *args, **kwargs):
        # Si el movimiento ya existe, revertir el movimiento anterior
        if self.pk is not None:
            old = MovimientoStock.objects.get(pk=self.pk)
            if old.type_choice == "entrada":
                self.product.current_stock -= old.amount
            elif old.type_choice == "salida":
                self.product.current_stock += old.amount

        # Validar si hay suficiente stock para una salida
        if self.type_choice == "salida" and self.amount > self.product.current_stock:
            raise ValidationError(
                f"No hay suficiente stock de '{self.product.name}' para realizar la salida."
            )

        # Aplicar el nuevo movimiento
        if self.type_choice == "entrada":
            self.product.current_stock += self.amount
        elif self.type_choice == "salida":
            self.product.current_stock -= self.amount

        self.product.save()
        super().save(*args, **kwargs)
