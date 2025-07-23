from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Cambio de nombre de la URL de admin a admin-login
    # Esto permite que los usuarios puedan acceder a la vista de administración de la APP
    path("admin-django/", admin.site.urls),
    path("", include("floristapp.urls")),  # Enrutamiento a la app
]
