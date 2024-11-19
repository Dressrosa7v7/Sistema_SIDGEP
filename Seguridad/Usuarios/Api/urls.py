from Confi.urls import path, include


urlpatterns = [
    path('Usuario/', include('apps.seguridad.usuarios.urls')),
]