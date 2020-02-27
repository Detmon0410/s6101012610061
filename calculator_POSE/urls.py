from django.urls import path

from . import views
from django.contrib import admin

urlpatterns = [
    # link path to views.py
    path('', views.index, name='index'),
    path('calc', views.index, name='calculate'),
    path('admin/', admin.site.urls),

]