from django.contrib import admin

# Register your models here.
from .models import (
    CategoriaProducto,
    Proveedor,
    Empleado,
    Almacen,
    Producto,
    MovimientoStock,
)

# Registro básico
admin.site.register(CategoriaProducto)
admin.site.register(Proveedor)
admin.site.register(Empleado)
admin.site.register(Almacen)


# Opcional: personalizar la vista de Producto en el admin
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "supplier", "current_stock", "unit")
    search_fields = ("name",)
    list_filter = ("category", "supplier")


# Opcional: personalizar la vista de MovimientoStock en el admin
@admin.register(MovimientoStock)
class MovimientoStockAdmin(admin.ModelAdmin):
    list_display = ("product", "type_choice", "amount", "date", "reason")
    search_fields = ("product__name", "reason")
    list_filter = ("type_choice", "date", "reason")
