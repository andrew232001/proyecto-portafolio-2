from django.contrib import admin
from django.urls import path, incluide

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', incluide('sistema_de_asistesia_DUOC_UC.urls'))
]