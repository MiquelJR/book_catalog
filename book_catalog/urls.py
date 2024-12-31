from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # Página de inicio
    path('books/', include('books.urls')),  # Incluye las URLs de la app books
]
