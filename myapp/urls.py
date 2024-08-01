from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos_view, name='productos'),
    path('ok/', views.ok_view, name='ok_view'),


]