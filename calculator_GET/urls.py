from django.urls import path

from . import views
from django.contrib import admin

urlpatterns = [
    # link path to views.py
    path('', views.index, name='index'),
    path('calcGET', views.calculateGET, name='calculate_get'),
    path('admin/', admin.site.urls),

]