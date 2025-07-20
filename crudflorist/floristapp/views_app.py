from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto, MovimientoStock
from .forms import ProductoForm, MovimientoStockForm


# PRODUCTOS


@login_required
def producto_list(request):
    productos = Producto.objects.select_related("category", "store", "supplier").all()
    return render(request, "app/producto_list.html", {"productos": productos})


@login_required
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "app/producto_detail.html", {"producto": producto})


@login_required
def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado exitosamente.")
            return redirect("producto_list")
    else:
        form = ProductoForm()
    return render(request, "app/producto_form.html", {"form": form})


@login_required
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado exitosamente.")
            return redirect("producto_list")
    else:
        form = ProductoForm(instance=producto)
    return render(request, "app/producto_form.html", {"form": form})


@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        messages.success(request, "Producto eliminado exitosamente.")
        return redirect("producto_list")
    return render(request, "app/producto_confirm_delete.html", {"producto": producto})


# MOVIMIENTOS DE STOCK
# Permitir solo acceso mediante login
@login_required
def movimiento_list(request):
    movimientos = MovimientoStock.objects.select_related(
        "product", "employee"
    ).order_by("-date")
    return render(request, "app/movimiento_list.html", {"movimientos": movimientos})


@login_required
def movimiento_create(request):
    if request.method == "POST":
        form = MovimientoStockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Movimiento registrado exitosamente.")
            return redirect("movimiento_list")
    else:
        form = MovimientoStockForm()
    return render(request, "app/movimiento_form.html", {"form": form})
