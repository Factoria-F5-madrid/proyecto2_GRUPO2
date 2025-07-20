from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test,
)
from .models import Producto, MovimientoStock


# Función para verificar si el usuario es admin o staff
def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)


# decoradores
@user_passes_test(is_admin)
@login_required
def dashboard_admin(request):
    total_productos = Producto.objects.count()
    total_stock = Producto.objects.aggregate(total=Sum("current_stock"))["total"] or 0
    productos_bajo_stock = Producto.objects.filter(current_stock__lt=5)
    ultimos_movimientos = MovimientoStock.objects.select_related("product").order_by(
        "-date"
    )[:5]

    context = {
        "total_productos": total_productos,
        "total_stock": total_stock,
        "productos_bajo_stock": productos_bajo_stock,
        "ultimos_movimientos": ultimos_movimientos,
    }

    return render(request, "admin/dashboard.html", context)


# alertas
@user_passes_test(is_admin)
@login_required
def alertas_bajo_stock(request):
    productos_bajo_stock = Producto.objects.filter(current_stock__lt=5)
    return render(
        request,
        "admin/alertas_stock.html",
        {"productos_bajo_stock": productos_bajo_stock},
    )


@user_passes_test(is_admin)
@login_required
def reporte_stock(request):
    productos = Producto.objects.all()
    return render(request, "admin/reporte_stock.html", {"productos": productos})
