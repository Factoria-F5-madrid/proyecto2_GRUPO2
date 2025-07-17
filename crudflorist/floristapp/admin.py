from django.contrib import admin
from .models import (
    CategoriaProducto,
    Proveedor,
    Empleado,
    Almacen,
    Producto,
    MovimientoStock,
)


@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
    search_fields = ("name", "email")
    list_filter = ("name",)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "hiring_date")
    search_fields = ("name",)
    list_filter = ("position", "hiring_date")


@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    search_fields = ("name", "location")


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "supplier", "store", "current_stock", "unit")
    search_fields = ("name", "description")
    list_filter = ("category", "supplier", "store")
    readonly_fields = ("current_stock",)  # evita modificarlo manualmente


@admin.register(MovimientoStock)
class MovimientoStockAdmin(admin.ModelAdmin):
    list_display = ("product", "type_choice", "amount", "date", "reason", "employee")
    search_fields = ("product__name", "reason", "observaciones")
    list_filter = ("type_choice", "date", "reason")
    date_hierarchy = "date"
