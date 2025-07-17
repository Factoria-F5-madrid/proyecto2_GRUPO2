from django import forms
from .models import Producto, MovimientoStock


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "purchase_price": forms.NumberInput(attrs={"class": "form-control"}),
            "sales_price": forms.NumberInput(attrs={"class": "form-control"}),
            "current_stock": forms.NumberInput(attrs={"class": "form-control"}),
            "unit": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "supplier": forms.Select(attrs={"class": "form-select"}),
            "store": forms.Select(attrs={"class": "form-select"}),
        }


class MovimientoStockForm(forms.ModelForm):
    class Meta:
        model = MovimientoStock
        fields = [
            "product",
            "type_choice",
            "amount",
            "reason",
            "employee",
            "observaciones",
        ]
        widgets = {
            "product": forms.Select(attrs={"class": "form-select"}),
            "type_choice": forms.Select(attrs={"class": "form-select"}),
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "reason": forms.TextInput(attrs={"class": "form-control"}),
            "employee": forms.Select(attrs={"class": "form-select"}),
            "observaciones": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
