from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.home),  # root URL
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]



