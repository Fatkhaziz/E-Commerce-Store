from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('user', include('clients.urls')),
    path('user', include('clients.urls'))
]
