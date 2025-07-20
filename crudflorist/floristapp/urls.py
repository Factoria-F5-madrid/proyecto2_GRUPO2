from django.urls import path
from . import views_app
from . import views_admin
from . import views_auth


urlpatterns = [
    # VISTA PRINCIPAL
    path("", views_auth.home_view, name="home"),
    # AUTENTICACIÓN
    path("login/", views_auth.login_view, name="login"),
    path("logout/", views_auth.logout_view, name="logout"),
    path("register/", views_auth.register_view, name="register"),
    # VISTAS DE USO GENERAL (USUARIOS)
    path("productos/", views_app.producto_list, name="producto_list"),
    path("productos/nuevo/", views_app.producto_create, name="producto_create"),
    path("productos/<int:pk>/", views_app.producto_detail, name="producto_detail"),
    path(
        "productos/<int:pk>/editar/", views_app.producto_update, name="producto_update"
    ),
    path("productos/<int:pk>/eliminar/", views_app.producto_delete, name="producto_delete"),
    path("movimientos/", views_app.movimiento_list, name="movimiento_list"),
    path("movimientos/nuevo/", views_app.movimiento_create, name="movimiento_create"),
    # VISTAS ADMINISTRATIVAS
    path("admin/dashboard/", views_admin.dashboard_admin, name="dashboard_admin"),
    path(
        "admin/alertas-stock/",
        views_admin.alertas_bajo_stock,
        name="alertas_bajo_stock",
    ),
    path("admin/reporte-stock/", views_admin.reporte_stock, name="reporte_stock"),
]
