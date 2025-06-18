from django.urls import path
from .views import login_view, home_view  # ← nuevo

urlpatterns = [
    path('', home_view),  # ← nueva ruta para "/"
    path('login/', login_view),
]
