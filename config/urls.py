
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de autenticación de Django
    path('cuentas/', include('django.contrib.auth.urls')),
]
