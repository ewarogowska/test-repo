from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('myapp/', include('myapp.urls')), # dołączamy reguły url z pliku myapp\urls.py
    path('admin/', admin.site.urls),
]
