
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tienda/', include('tienda.urls')),
    path('admin/', admin.site.urls),
]
