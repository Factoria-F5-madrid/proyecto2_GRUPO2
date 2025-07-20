from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return float(value) * float(arg)

@register.filter
def sum_column(productos, column_name):
    total = 0
    for producto in productos:
        if column_name == 'total_compra':
            total += float(producto.purchase_price) * producto.current_stock
        elif column_name == 'total_venta':
            total += float(producto.sales_price) * producto.current_stock
    return total

# Añadir estos nuevos filtros
@register.filter
def sub(value, arg):
    return float(value) - float(arg)

@register.filter
def mul(value, arg):
    return float(value) * float(arg)

@register.filter
def div(value, arg):
    if float(arg) == 0:
        return 0
    return float(value) / float(arg)
